import datetime
import functools
import inspect
import itertools
import re
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Dict,
    FrozenSet,
    Generic,
    Iterable,
    List,
    Optional as T_Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
    overload,
)

import attr
from dateutil import parser

from cleanchausie.consts import EMPTY, OMITTED, empty, omitted
from cleanchausie.utils import getter

if TYPE_CHECKING:
    from .schema import Schema


@attr.frozen
class ValidationError:
    errors: List["Error"]

    def serialize(self) -> Dict:
        """Serialize field-level errors dict.

        This is useful for rest responses and test assertions.
        """
        return {
            "errors": [{"msg": e.msg, "field": e.field} for e in self.errors]
        }


@attr.frozen
class Error:
    msg: str
    field: Tuple[Union[str, int], ...] = ()


@attr.frozen
class Errors:
    errors: List[Error]
    field: Tuple[Union[str, int], ...] = ()

    def flatten(self) -> List[Error]:
        return [
            wrap_result(field=self.field, result=err) for err in self.errors
        ]


T = TypeVar("T")


@attr.frozen
class Value(Generic[T]):
    value: T


V = TypeVar("V")


@attr.frozen
class UnvalidatedWrappedValue(Generic[T, V]):
    value: Collection[V]
    inner_field: "Field[T]"

    construct: Callable
    """Called to construct the wrapped type with validated data."""


UnvalidatedMappedKeyType = TypeVar("UnvalidatedMappedKeyType")
UnvalidatedMappedValueType = TypeVar("UnvalidatedMappedValueType")


@attr.frozen
class UnvalidatedMappedValue(
    Generic[UnvalidatedMappedKeyType, UnvalidatedMappedValueType]
):
    value: Dict
    key_field: T_Optional["Field[UnvalidatedMappedKeyType]"]
    value_field: T_Optional["Field[UnvalidatedMappedValueType]"]

    construct: Callable
    """Called to construct the mapping type with validated data."""


class Nullability:
    allow_none: bool


@attr.frozen
class Required(Nullability):
    allow_none: bool = False


@attr.frozen
class Omittable(Nullability):
    allow_none: bool = True
    omitted_value_factory: Union[OMITTED, Callable] = omitted
    omitted_value: Any = omitted


@overload
def wrap_result(field: Tuple[Union[str, int], ...], result: Error) -> Error:
    ...


@overload
def wrap_result(field: Tuple[Union[str, int], ...], result: Value) -> Value:
    ...


def wrap_result(
    field: Tuple[Union[str, int], ...], result: Any
) -> Union[Value, Error]:
    if isinstance(result, Error):
        return attr.evolve(result, field=field + result.field)
    elif not isinstance(result, Value):
        return Value(value=result)
    return result


FieldReturnType = TypeVar("FieldReturnType")


def _get_deps(func: Callable) -> Set[str]:
    return set(inspect.signature(func).parameters.keys())


def inject_deps(
    func: Callable,
    val: Any,
    context: Any,
    intermediate_results: Dict[str, Any],
    root_value: Any,
) -> Callable:
    deps = _get_deps(func)
    if not deps:
        return func

    # an empty context default value means its optional/passthrough
    if (
        "context" in deps
        and context is empty
        and inspect.signature(func).parameters["context"].default is not empty
    ):
        raise ValueError("Context is required for evaluating this schema.")

    return functools.partial(
        func,
        **{
            dep: v.value
            for dep, v in intermediate_results.items()
            if dep in deps
        },
        **{
            dep: v
            for dep, v in {
                "context": context,
                "value": val,
                "root_value": root_value,
                "intermediate_results": intermediate_results,
            }.items()
            if dep in deps
        },
    )


@attr.frozen
class Field(Generic[FieldReturnType]):
    validators: Tuple[Callable, ...]
    """Callable that validate a the given field's value."""

    accepts: T_Optional[Tuple[str, ...]]
    """Field names accepted when parsing unvalidated input.

    If left unspecified, defaults to the name of the attribute defined on the
    schema. It can be explicitly set to `None` to force the schema to not
    accept any input. This can be useful for validation-only fields or derived
    fields.
    """

    serialize_to: T_Optional[str]
    """If provided overrides the name of the field during serialization."""

    serialize_func: Callable[[Any], Any]
    """Used when serializing this field. Defaults to a noop passthrough."""

    nullability: Nullability

    depends_on: Tuple[str, ...]
    """Other fields on the same schema this field depends on"""

    # lets mypy and IDE's autocomplete/resolve to the right type
    def __get__(self, instance, owner) -> FieldReturnType:  # type: ignore[empty-body]
        ...

    def run_validators(
        self,
        field: Tuple[Union[str, int], ...],
        root_value: Any,
        value: Any,
        context: Any,
        intermediate_results: Dict[str, Any],
    ) -> Union[Value[FieldReturnType], Errors]:
        # handle nullability
        if value in (omitted, None) and any(
            ["value" in _get_deps(v) for v in self.validators]
        ):
            if value is None:
                if self.nullability.allow_none:
                    return Value(cast(FieldReturnType, value))
                else:
                    if isinstance(self.nullability, Required):
                        msg = "This field is required, and must not be None."
                    else:
                        msg = "This field must not be None."

                    return Errors(field=field, errors=[Error(msg=msg)])

            if isinstance(self.nullability, Required):
                return Errors(
                    field=field, errors=[Error(msg="This field is required.")]
                )
            elif isinstance(self.nullability, Omittable):
                return Value(
                    self.nullability.omitted_value_factory()
                    if not isinstance(
                        self.nullability.omitted_value_factory, OMITTED
                    )
                    else self.nullability.omitted_value
                )
            else:
                raise TypeError

        result = value
        for validator in self.validators:
            result = inject_deps(
                func=validator,
                val=result,
                context=context,
                intermediate_results=intermediate_results,
                root_value=root_value,
            )()
            if isinstance(result, UnvalidatedWrappedValue):
                result = validate_wrapped_value_result(
                    result=result,
                    root_value=root_value,
                    context=context,
                    intermediate_results=intermediate_results,
                )
            elif isinstance(result, UnvalidatedMappedValue):
                result = validate_mapped_value_result(
                    result=result,
                    root_value=root_value,
                    context=context,
                    intermediate_results=intermediate_results,
                )

            if isinstance(result, (Error, Errors)):
                if self.accepts is None and not result.field:
                    # ignore the last part of the path if this field isn't
                    # directly based on any input field
                    err_field = field[:-1]
                else:
                    err_field = result.field or field

                if isinstance(result, Errors):
                    errors = result.flatten()
                else:
                    errors = [Error(msg=result.msg)]
                return Errors(field=err_field, errors=errors)

        return wrap_result(field=field, result=result)


def validate_wrapped_value_result(
    result: UnvalidatedWrappedValue,
    root_value: Any,
    context: Any,
    intermediate_results: Dict[str, Any],
) -> Union[Value, Errors]:
    inner_results = [
        result.inner_field.run_validators(
            field=(idx,),
            root_value=root_value,
            value=inner_value,
            context=context,
            intermediate_results=intermediate_results,
        )
        for idx, inner_value in enumerate(result.value)
    ]
    flattened_errors = []
    for r in inner_results:
        if isinstance(r, Errors):
            flattened_errors.extend(r.flatten())
    if flattened_errors:
        return Errors(errors=flattened_errors)

    # construct result with the validated inner data
    return result.construct(inner_results)


def validate_mapped_value_result(
    result: UnvalidatedMappedValue,
    root_value: Any,
    context: Any,
    intermediate_results: Dict[str, Any],
) -> Union[Value, Errors]:
    if result.key_field:
        key_results = [
            result.key_field.run_validators(
                field=(f"{key} (key)",),
                root_value=root_value,
                value=key,
                context=context,
                intermediate_results=intermediate_results,
            )
            for key in result.value.keys()
        ]
    else:
        key_results = [Value(k) for k in result.value.keys()]

    if result.value_field:
        value_results = [
            result.value_field.run_validators(
                field=(f"{key} (value)",),
                root_value=root_value,
                value=value,
                context=context,
                intermediate_results=intermediate_results,
            )
            for key, value in result.value.items()
        ]
    else:
        value_results = [Value(v) for v in result.value.values()]

    flattened_errors = []
    for r in key_results + value_results:
        if isinstance(r, Errors):
            flattened_errors.extend(r.flatten())
    if flattened_errors:
        return Errors(errors=flattened_errors)

    # construct result with the validated key/value pairs
    return result.construct(tuple(zip(key_results, value_results)))


def noop(value: V) -> V:
    return value


# to avoid func calls in args. Effectively the same thing, but required is
# not mutable, so it shouldn't matter.
required = Required()


FType = TypeVar("FType")
ParentsAnnotation = Union[
    Union[Callable, Field[Any]], Tuple[Union[Callable, Field[Any]], ...]
]


# when decorating a function (decorated func is passed to the inner func)
@overload
def field(
    *,
    parents: ParentsAnnotation = (),
    accepts: T_Optional[Tuple[str, ...]] = (),
    serialize_to: T_Optional[str] = None,
    serialize_func: T_Optional[Callable] = None,
    nullability: Nullability = required,
) -> Callable[
    [Union[Callable[..., Union[Error, Errors, FType]], Callable[..., FType]]],
    Field[FType],
]:
    ...


# defining simple fields with existing functions
@overload
def field(
    decorated_func: Callable[..., Union[Error, Errors, FType]],
    *,
    parents: ParentsAnnotation = (),
    accepts: T_Optional[Tuple[str, ...]] = (),
    serialize_to: T_Optional[str] = None,
    serialize_func: T_Optional[Callable] = None,
    nullability: Nullability = required,
) -> Field[FType]:
    ...


@overload
def field(
    decorated_func: Field[FType],
    *,
    parents: ParentsAnnotation = (),
    accepts: T_Optional[Tuple[str, ...]] = (),
    serialize_to: T_Optional[str] = None,
    serialize_func: T_Optional[Callable] = None,
    nullability: Nullability = required,
) -> Field[T_Optional[FType]]:
    ...


def field(
    decorated_func: T_Optional[
        Union[Callable[..., Union[Error, Errors, FType]], Field[FType]]
    ] = None,
    *,
    parents: ParentsAnnotation = (),
    accepts: T_Optional[Tuple[str, ...]] = (),
    serialize_to: T_Optional[str] = None,
    serialize_func: T_Optional[Callable] = None,
    nullability: Nullability = required,
) -> Union[
    Callable[
        [
            Union[
                Callable[..., Union[Error, Errors, FType]],
                Callable[..., FType],
            ]
        ],
        Field[FType],
    ],
    Field[FType],
    Field[T_Optional[FType]],
]:
    """Defines a Field.

    Args:
        decorated_func: The only accepted positional arg, must be either a
            callable or a `Field` instance.
        parents: Optionally a tuple of any parent fields. Validated values chain between
            parents in order they've been given here, before being passed to this
            field's validation function. Note that if a `Field` is given instead of a
            `Callable`, only the validators are reused.
        accepts: Optionally a tuple of field names to accept values from. If not given,
            defaults to the field name on the schema. Field names given first are given
            precedent. Can be set to an explicit `None` to signal no value should
            be accepted for this field.
        serialize_to: The field name to serialize to. Defaults to the field name on the
            schema.
        serialize_func: Optionally a function that transforms the serialized value
            during serialization. Defaults to noop, which passes through the value
            unchanged.
        nullability: An instance of one of `Nullability`'s descendants, used to define
            behavior if a field is omitted or falsy. Defaults to Required.
    """
    # make it a little more convenient for cases where there's only one parent
    wrapped_parents = parents if isinstance(parents, tuple) else (parents,)

    if decorated_func is not None:
        if isinstance(decorated_func, Field):
            return _outer_field(
                inner_func=noop,
                parents=wrapped_parents + (decorated_func,),
                accepts=accepts,
                serialize_to=serialize_to,
                serialize_func=(
                    serialize_func or decorated_func.serialize_func
                ),
                nullability=nullability,
            )
        else:
            return _outer_field(
                inner_func=decorated_func,
                parents=wrapped_parents,
                accepts=accepts,
                serialize_to=serialize_to,
                serialize_func=serialize_func or noop,
                nullability=nullability,
            )

    else:

        def _wrap(
            inner_func: Callable[..., Union[Error, Errors, FType]]
        ) -> Field[FType]:
            return _outer_field(
                inner_func,
                parents=wrapped_parents,
                accepts=accepts,
                serialize_to=serialize_to,
                serialize_func=serialize_func or noop,
                nullability=nullability,
            )

        return _wrap


def _outer_field(
    inner_func: Callable[..., Union[Error, Errors, FType]],
    *,
    parents: Tuple[Union[Callable, Field], ...] = (),
    accepts: T_Optional[Tuple[str, ...]] = (),
    serialize_to: T_Optional[str] = None,
    serialize_func: Callable = noop,
    nullability: Nullability = required,
) -> Field[FType]:
    # flatten any parents defined as fields
    validators: List[Callable] = []
    for p in parents + (inner_func,):
        if isinstance(p, Field):
            validators.extend(p.validators)
        else:
            validators.append(p)

    # find any declared dependencies on other fields
    deps = {
        n
        for n in itertools.chain(
            *[inspect.signature(f).parameters.keys() for f in validators]
        )
        if n not in {"context", "value", "root_value", "intermediate_results"}
    }
    f: Field[FType] = Field(
        nullability=nullability,
        validators=tuple(validators),
        accepts=accepts,
        serialize_to=serialize_to,
        serialize_func=serialize_func,
        depends_on=tuple(deps),
    )
    return f


def clean_field(
    field: Field[T], data: Any, context: Any = empty
) -> Union[T, ValidationError]:
    """Validate data using a specific field.

    This can be helpful for defining reusable fields, or for using complex
    fields as top-level schemas as well.
    """
    result = field.run_validators(
        field=(),
        root_value=data,
        value=data,
        context=context,
        intermediate_results={},
    )
    if isinstance(result, Errors):
        return ValidationError(result.flatten())
    return result.value


def serialize_field(field: Field[T], value: T) -> Any:
    """Serialize a value using a specific field.

    It's assumed that the value has already been validated.
    """
    return field.serialize_func(value)


def IntField(  # noqa: N802
    min_value: Union[EMPTY, int] = empty, max_value: Union[EMPTY, int] = empty
) -> Field[int]:
    def _intfield(value: Any) -> Union[int, Error]:
        """Simple string coercion/validation for int values."""
        # coerce from string if needed
        if isinstance(value, int):
            return value
        elif isinstance(value, str):
            try:
                return int(value)
            except (ValueError, TypeError):
                return Error(msg="Unable to parse int from given string.")

        return Error(msg=f"Unhandled type '{type(value)}', could not coerce.")

    def _min(value: int) -> Union[int, Error]:
        if not isinstance(min_value, EMPTY) and value < min_value:
            return Error(
                msg=f"Value must be greater than or equal to {min_value}."
            )
        return value

    def _max(value: int) -> Union[int, Error]:
        if not isinstance(max_value, EMPTY) and value > max_value:
            return Error(
                msg=f"Value must be less than or equal to {max_value}."
            )
        return value

    return field(noop, parents=(_intfield, _min, _max))


def StrField(  # noqa: N802
    min_length: Union[EMPTY, int] = empty,
    max_length: Union[EMPTY, int] = empty,
) -> Field[str]:
    """Simple validation for str values."""

    def _strfield(value: Any) -> Union[str, Error]:
        if isinstance(value, str):
            return value

        return Error(msg=f"Unhandled type '{type(value)}'")

    def _min(value: str) -> Union[str, Error]:
        if not isinstance(min_length, EMPTY) and len(value) < min_length:
            return Error(
                msg=f"Length must be greater than or equal to {min_length}."
            )
        return value

    def _max(value: str) -> Union[str, Error]:
        if not isinstance(max_length, EMPTY) and len(value) > max_length:
            return Error(
                msg=f"Length must be less than or equal to {max_length}."
            )
        return value

    return field(noop, parents=(_strfield, _min, _max))


def ListField(  # noqa: N802
    inner_field: Field[T], max_length: Union[EMPTY, int] = empty
) -> Field[List[T]]:
    def _call(
        value: Any, root_value, intermediate_results, context=empty
    ) -> Union[List[T], Error, Errors]:
        result = _impl(value)
        if not isinstance(result, (Error, Errors)):
            inner_results = [
                inner_field.run_validators(
                    field=(idx,),
                    root_value=root_value,
                    value=inner_value,
                    context=context,
                    intermediate_results=intermediate_results,
                )
                for idx, inner_value in enumerate(value)
            ]
            flattened_errors = []
            for r in inner_results:
                if isinstance(r, Errors):
                    flattened_errors.extend(r.flatten())
            if flattened_errors:
                return Errors(errors=flattened_errors)
            else:
                # construct result with the validated inner data
                result = [
                    v.value for v in inner_results if not isinstance(v, Errors)
                ]
        return result

    def _impl(value: Any) -> Union[List[T], Error]:
        if isinstance(value, tuple):
            value = list(value)

        if isinstance(value, list):
            if isinstance(max_length, int) and len(value) > max_length:
                return Error(msg=f"Must be no more than {max_length} items.")

            return value

        return Error(msg="Unhandled type")

    return field(_call)


NestedFieldType = TypeVar("NestedFieldType", bound="Schema")


def NestedField(  # noqa: N802
    inner_schema: Type[NestedFieldType],
) -> Field[NestedFieldType]:
    def _call(
        value: Any, context: Any = empty
    ) -> Union[NestedFieldType, Errors]:
        result = inner_schema.clean(value, context=context)
        if isinstance(result, ValidationError):
            return Errors(errors=result.errors)
        elif isinstance(result, inner_schema):
            return result

        raise TypeError

    def _serialize_fn(value: NestedFieldType) -> Dict:
        return value.serialize()

    return field(_call, serialize_func=_serialize_fn)


DictKeyType = TypeVar("DictKeyType")
DictValueType = TypeVar("DictValueType")


class DictField(Generic[DictKeyType, DictValueType]):
    key_field: T_Optional[Field[DictKeyType]]
    value_field: T_Optional[Field[DictValueType]]

    def __init__(
        self,
        key_field: T_Optional[Field[DictKeyType]],
        value_field: T_Optional[Field[DictValueType]],
    ) -> None:
        self.key_field = key_field
        self.value_field = value_field

    def __call__(
        self, value: Any, context: Any = empty
    ) -> Union[
        UnvalidatedMappedValue[DictKeyType, DictValueType], Error, Errors
    ]:
        if not isinstance(value, dict):
            return Error("Value is not a dictionary")
        return UnvalidatedMappedValue(
            value=value,
            # these casts directly line up with the value on the type, which
            # mypy reads incorrectly for some reason.
            key_field=cast(T_Optional[Field[DictKeyType]], self.key_field),
            value_field=cast(
                T_Optional[Field[DictValueType]], self.value_field
            ),
            construct=self.construct,
        )

    @staticmethod
    def construct(
        mapped_pairs: List[Tuple[Value, Value]]
    ) -> Dict[DictKeyType, DictValueType]:
        return {k.value: v.value for k, v in mapped_pairs}


EnumCls = TypeVar("EnumCls", bound=Enum)


class EnumField(Generic[EnumCls]):
    enum_cls: Type[EnumCls]
    valid_options: FrozenSet[EnumCls]

    def __init__(
        self,
        enum_cls: Type[EnumCls],
        valid_options: Union[Iterable[EnumCls], EMPTY] = empty,
    ) -> None:
        self.enum_cls = enum_cls
        if not isinstance(valid_options, EMPTY):
            self.valid_options = frozenset(valid_options)
        else:
            self.valid_options = frozenset()

    def __call__(self, value: Any) -> Union[EnumCls, Error]:
        options = self.valid_options if self.valid_options else self.enum_cls
        # mypy doesn't let us express `EnumType[EnumCls]`, so it thinks there's
        # no `__iter__` on `enum_cls`
        option_strings = sorted([str(o.value) for o in options])  # type: ignore
        err_msg = f"Value must be one of: {', '.join(option_strings)}"
        try:
            enum_val = self.enum_cls(value)
        except (ValueError, TypeError):
            return Error(msg=err_msg)

        if self.valid_options and enum_val not in self.valid_options:
            return Error(msg=err_msg)

        return enum_val


def RegexField(regex: str, flags: int = 0) -> Field[str]:  # noqa: N802
    _compiled_regex = re.compile(regex, flags)

    def _validate_regex(value: str) -> Union[str, Error]:
        if not _compiled_regex.match(value):
            return Error(msg="Invalid input.")
        return value

    return field(_validate_regex, parents=(StrField(),))


def DateTimeField() -> Field[datetime.datetime]:  # noqa: N802
    @field(parents=(StrField(),))
    def _datetimefield(value: str) -> Union[Error, datetime.datetime]:
        # TODO should this reject naive datetimes? or assume a timezone?
        try:
            # TODO should we use ciso8601 to parse? It's a bit stricter, but much faster.
            return parser.parse(value)
        except ValueError:
            return Error(msg="Could not parse datetime.")

    return _datetimefield


def BoolField() -> Field[bool]:  # noqa: N802
    @field
    def _boolfield(value: Any) -> Union[bool, Error]:
        if not isinstance(value, bool):
            return Error(msg="Value is not a boolean.")
        return value

    return _boolfield


def URLField(  # noqa: N802
    require_tld=True,
    default_scheme=None,
    allowed_schemes=None,
    disallowed_schemes=None,
) -> Field[str]:
    def normalize_scheme(sch):
        if sch.endswith("://") or sch.endswith(":"):
            return sch
        return sch + "://"

    # FQDN validation similar to https://github.com/chriso/validator.js/blob/master/src/lib/isFQDN.js

    # ff01-ff5f -> full-width chars, not allowed
    alpha_numeric_and_symbols_ranges = "0-9a-z\u00a1-\uff00\uff5f-\uffff"

    tld_part = (
        require_tld
        and r"\.[{}-]{{2,63}}".format(alpha_numeric_and_symbols_ranges)
        or ""
    )
    scheme_part = "[a-z]+://"
    if default_scheme:
        default_scheme = normalize_scheme(default_scheme)
    scheme_regex = re.compile("^" + scheme_part, re.IGNORECASE)
    if default_scheme:
        scheme_part = f"({scheme_part})?"
    regex = r"^{}([-{}@:%%_+.~#?&/\\=]{{1,256}}{}|([0-9]{{1,3}}\.){{3}}[0-9]{{1,3}})(:[0-9]+)?([/?].*)?$".format(
        scheme_part, alpha_numeric_and_symbols_ranges, tld_part
    )
    regex_flags = re.IGNORECASE | re.UNICODE

    def compile_schemes_to_regexes(schemes):
        return [
            re.compile("^" + normalize_scheme(sch) + ".*", re.IGNORECASE)
            for sch in schemes
        ]

    allowed_schemes = allowed_schemes or []
    allowed_schemes_regexes = compile_schemes_to_regexes(allowed_schemes)

    disallowed_schemes = disallowed_schemes or []
    disallowed_schemes_regexes = compile_schemes_to_regexes(disallowed_schemes)

    @field(parents=(RegexField(regex=regex, flags=regex_flags),))
    def _urlfield(value: str) -> Union[Error, str]:
        if not scheme_regex.match(value):
            value = default_scheme + value

        if allowed_schemes:
            if not any(
                allowed_regex.match(value)
                for allowed_regex in allowed_schemes_regexes
            ):
                allowed_schemes_text = " or ".join(allowed_schemes)
                return Error(
                    msg=(
                        "This URL uses a scheme that's not allowed. You can only "
                        f"use {allowed_schemes_text}."
                    )
                )

        if disallowed_schemes:
            if any(
                disallowed_regex.match(value)
                for disallowed_regex in disallowed_schemes_regexes
            ):
                return Error(msg="This URL uses a scheme that's not allowed.")

        return value

    return _urlfield


def EmailField(max_length=254) -> Field[str]:  # noqa: N802
    email_regex = (
        r"^(?:[^\.@\s]|[^\.@\s]\.(?!\.))*[^.@\s]@"
        r"[^.@\s](?:[^\.@\s]|\.(?!\.))*\.[a-z]{2,63}$"
    )
    regex_flags = re.IGNORECASE

    def _email_field(value: str) -> Union[str, Error]:
        # trim any leading/trailing whitespace before validating the email
        ret = value.strip()

        # only allow up to max_length
        if len(ret) > max_length:
            return Error(f"Email exceeds max length of {max_length}")

        return ret

    return field(
        noop,
        parents=(
            StrField(),
            _email_field,
            RegexField(regex=email_regex, flags=regex_flags),
        ),
    )


def PolymorphicField(  # noqa: N802
    type_field: str,
    type_map: Dict[Any, Type["Schema"]],
    default_type_key: Any = empty,
) -> Field:
    """Map to different schemas based on a tagged type.

    This is useful for cases where different incompatible structures may be
    used, and which structure to validate against is tagged explicitly by a
    field.

    For example, we may want to validate "foo" and "bar" type items
    differently:
        [{"type": "foo", "foo": "bar"}, {"type": "bar", "bar": 1}]

    This would be possible with a field like:
        List(
            PolymorphicField(
                type_field="type",
                type_map={
                    "foo": Schema({"foo": Str()}),
                    "bar": Schema({"bar": Int()}),
                },
            )
        )

    Args:
        type_field: The field name that contains the type tag.
        type_map: A mapping of type tags to schemas.
        default_type_key: The default type tag to use if the type field is
            omitted.
    """

    @field
    def _polymorphic_field(
        value: Any, context: Any = empty
    ) -> Union["Schema", Errors]:
        type_val = getter(value, type_field, omitted)
        if type_val is omitted:
            if default_type_key is not empty:
                type_val = default_type_key
            else:
                # nested object does not have the type field
                return Errors(
                    errors=[
                        Error(
                            f"Required type field '{type_field}' not provided"
                        )
                    ]
                )

        inner_schema = type_map.get(type_val, empty)
        if isinstance(inner_schema, EMPTY):
            return Errors(errors=[Error(f"Type '{type_val}' is not handled.")])

        result = inner_schema.clean(value, context=context)
        if isinstance(result, ValidationError):
            return Errors(errors=result.errors)
        elif isinstance(result, inner_schema):
            return result

        raise TypeError

    return _polymorphic_field


@attr.frozen
class PolySchemaMapping(Generic[T]):
    public_type: str
    internal_type: Type[T]
    serializer: Callable[[T], Dict]
    clean: Callable[[Any, Any], Union[T, ValidationError]]


def SerializablePolymorphicField(  # noqa: N802
    type_field: str,
    mappings: Iterable[PolySchemaMapping[T]],
    default_type_key: Any = empty,
) -> Field[T]:
    """Similar to PolymorphicField, but also supports serialization.

    This is useful for cases where different incompatible structures may be
    used, and which structure to validate against is tagged explicitly by a
    field.

    As part of supporting more advanced serialization and parsing, the end
    result for validated values will generally be an instance of an internal
    type rather than of a schema. As such, explicit `internal_type`,
    `factory`, and `serializer` functions must be provided for each mapping.

    For example, we may want to validate "foo" and "bar" type items to
    internal types Foo and Bar, respectively:
        [{"type": "foo", "foo": "bar"}, {"type": "bar", "bar": 1}]

    This would be possible with a field like:
        SerializablePolymorphicField(
            type_field="type",
            mappings=[
                PolySchemaMapping(
                    public_type="foo",
                    internal_type=Foo,
                    schema_cls=Schema({"foo": Str()}),
                    serializer=lambda foo: {"foo": foo.foo},
                    factory=lambda schema: Foo(foo=schema.foo),
                ),
                PolySchemaMapping(
                    public_type="bar",
                    internal_type=Bar,
                    schema_cls=Schema({"bar": Int()}),
                    serializer=lambda bar: {"bar": bar.bar},
                    factory=lambda schema: Bar(bar=schema.bar),
                ),
            ],
        )

    Args:
        type_field: The field name that contains the type tag.
        mappings: A list of PolySchemaMapping's that link public type tags,
            schemas, and internal types.
        default_type_key: The default type tag to use if the type field is
            omitted.
    """

    def _get_mapping(public_type: str) -> Union[PolySchemaMapping[T], EMPTY]:
        return next(
            (m for m in mappings if m.public_type == public_type), empty
        )

    def _serialize_func(value):
        if value is None:
            return None
        mapping = next(
            m for m in mappings if isinstance(value, m.internal_type)
        )
        result = mapping.serializer(value)
        if isinstance(result, dict):
            result[type_field] = mapping.public_type
        return result

    @field(serialize_func=_serialize_func)
    def _polymorphic_field(
        value: Any, context: Any = empty
    ) -> Union["T", Errors]:
        type_val = getter(value, type_field, omitted)
        if type_val is omitted:
            if default_type_key is not empty:
                type_val = default_type_key
            else:
                # nested object does not have the type field
                return Errors(
                    errors=[
                        Error(
                            f"Required type field '{type_field}' not provided"
                        )
                    ]
                )

        mapping = _get_mapping(type_val)
        if isinstance(mapping, EMPTY):
            return Errors(errors=[Error(f"Type '{type_val}' is not handled.")])

        result = mapping.clean(value, context)
        if isinstance(result, ValidationError):
            return Errors(errors=result.errors)
        elif isinstance(result, mapping.internal_type):
            return result

        raise TypeError

    return _polymorphic_field


def TimeDeltaField() -> Field[datetime.timedelta]:  # noqa: N802
    @field
    def _timedelta_field(
        value: Union[int, datetime.timedelta]
    ) -> datetime.timedelta:
        # value is either already a timedelta or is an int in seconds
        if isinstance(value, datetime.timedelta):
            return value
        elif isinstance(value, int):
            return datetime.timedelta(seconds=value)
        else:
            raise TypeError(f"Unhandled type '{type(value)}'")

    return _timedelta_field


def InstanceField(of_type: Type[T]) -> Field[T]:  # noqa: N802
    @field
    def _instance_field(value: Any) -> Union[T, Error]:
        if isinstance(value, of_type):
            return value
        return Error(f"Expected an object of type {of_type.__name__}")

    return _instance_field


FIELD_TYPE_MAP: Dict[type, Field] = {
    int: IntField(),
    str: StrField(),
    bool: BoolField(),
    datetime.datetime: DateTimeField(),
    datetime.timedelta: TimeDeltaField(),
}

FMapType = TypeVar("FMapType")


def get_field_for_basic_type(basic_type: Type[FMapType]) -> Field[FMapType]:
    return FIELD_TYPE_MAP[basic_type]
