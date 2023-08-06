import enum
import functools
import inspect
from typing import (
    Any,
    ClassVar,
    Dict,
    Optional,
    Type,
    TypeVar,
    Union,
    get_args,
    get_origin,
)

import cleancat.base

from cleanchausie.consts import OMITTED, empty
from cleanchausie.fields import (
    FIELD_TYPE_MAP,
    DictField,
    EnumField,
    Error,
    Field,
    ListField,
    Nullability,
    Omittable,
    Required,
    ValidationError,
    field,
    get_field_for_basic_type,
)
from cleanchausie.schema_definition import SchemaDefinition, clean, serialize


def field_def_from_annotation(annotation) -> Optional[Field]:
    """Turn an annotation into an equivalent field.

    Explicitly ignores `ClassVar` annotations, returning None.
    """
    if annotation in FIELD_TYPE_MAP:
        return get_field_for_basic_type(annotation)
    elif get_origin(annotation) is Union:
        # basic support for `Optional` and `OMITTED`
        union_of = get_args(annotation)

        # Handle explicitly omittable fields (`Union[T, OMITTED]`)
        if OMITTED in union_of:
            non_omitted_types = tuple(u for u in union_of if u is not OMITTED)
            if len(non_omitted_types) > 1:
                # create union without OMITTED
                inner_field = field_def_from_annotation(
                    Union[non_omitted_types]
                )
            else:
                inner_field = field_def_from_annotation(non_omitted_types[0])
            if inner_field is None:
                return None
            return field(
                inner_field,
                nullability=Omittable(
                    allow_none=inner_field.nullability.allow_none
                ),
            )

        # Otherwise, we only support `Optional[T]` annotations
        if not (len(union_of) == 2 and type(None) in union_of):
            raise TypeError("Unrecognized type annotation.")

        # yes, we actually do want to check against type(None)
        NoneType = type(None)
        inner = next(t for t in get_args(annotation) if t is not NoneType)
        inner_field = field_def_from_annotation(inner)
        if not inner_field:
            return None
        return field(inner_field, nullability=Required(allow_none=True))
    elif get_origin(annotation) is list:
        list_of = get_args(annotation)
        if len(list_of) != 1:
            raise TypeError("Only one inner List type is currently supported.")
        inner_field_def = field_def_from_annotation(list_of[0])
        assert inner_field_def
        return field(ListField(inner_field_def))
    elif get_origin(annotation) is dict:
        dict_of = get_args(annotation)
        if len(dict_of) == 2:
            key_field_def = field_def_from_annotation(dict_of[0])
            value_field_def = field_def_from_annotation(dict_of[1])
        elif len(dict_of) == 0:
            key_field_def = None
            value_field_def = None
        else:
            raise TypeError("Unrecognized type annotation.")
        return field(
            DictField(key_field=key_field_def, value_field=value_field_def)
        )
    elif inspect.isclass(annotation) and issubclass(annotation, enum.Enum):
        return field(EnumField(annotation))
    elif get_origin(annotation) is ClassVar:
        # just ignore these, these don't have to become fields
        return None

    raise TypeError(f"Unrecognized type annotation: '{repr(annotation)}'.")


def _field_def_from_old_field(f: cleancat.base.Field) -> Field:
    @functools.wraps(f.clean)
    def clean(*args, **kwargs):
        try:
            return f.clean(*args, **kwargs)
        except cleancat.base.ValidationError as e:
            return Error(msg=e.args and e.args[0])
        except cleancat.base.StopValidation as e:
            return e.args and e.args[0]

    # Cleancat fields are not really required if they have a
    # default, even if they have `required` set to True.
    nullability: Nullability = (
        Required()
        if f.required and f.default is None
        else Omittable(omitted_value_factory=lambda: clean(None))
    )

    return field(clean, serialize_func=f.serialize, nullability=nullability)


def _check_for_dependency_loops(fields: Dict[str, Field]) -> None:
    """Try to catch simple top-level dependency loops.

    Does not handle wrapped fields.
    """
    deps = {name: set(f_def.depends_on) for name, f_def in fields.items()}
    seen = {"self"}
    while deps:
        prog = len(seen)
        for f_name, f_deps in deps.items():
            if not f_deps or all([f_dep in seen for f_dep in f_deps]):
                seen.add(f_name)
                deps.pop(f_name)
                break

        if len(seen) == prog:
            # no progress was made
            raise ValueError(
                "Field dependencies could not be resolved. "
                f"Seen fields: {seen}; Remaining Deps: {deps}"
                "\nAre you missing parenthesis on the field?"
            )


class SchemaMetaclass(type):
    def __new__(cls, clsname, bases, attribs, autodef=True):
        """
        Turn a Schema subclass into a schema.

        Args:
            clsname: name of the class
            bases: base classes
            attribs: attributes defined on the class
            autodef: automatically define simple fields for annotated attributes
        """
        fields = {}
        for base in bases:
            # can't directly check for Schema class, since sometimes it hasn't
            # been created yet
            base_schema_def = getattr(base, "_schema_definition", None)
            if isinstance(base_schema_def, SchemaDefinition):
                fields.update(base_schema_def.fields)
        fields.update(
            {
                f_name: f
                for f_name, f in attribs.items()
                if isinstance(f, Field)
            }
        )

        # look for fields from the old cleancat schema
        fields.update(
            {
                f_name: _field_def_from_old_field(f)
                for f_name, f in attribs.items()
                if f_name not in fields and isinstance(f, cleancat.base.Field)
            }
        )

        if autodef:
            for f_name, f_type in attribs.get("__annotations__", {}).items():
                if f_name not in fields:
                    inner_field_def = field_def_from_annotation(f_type)
                    if not inner_field_def:
                        continue

                    if f_name in attribs:
                        # we have a default value, which means this is
                        # omittable
                        nullability: Nullability = Omittable(
                            allow_none=(
                                inner_field_def.nullability.allow_none
                                or attribs[f_name] is None
                            ),
                            omitted_value=attribs[f_name],
                        )
                    else:
                        nullability = inner_field_def.nullability

                    fields[f_name] = field(
                        inner_field_def, nullability=nullability
                    )

        # check for dependency loops
        _check_for_dependency_loops(fields)

        schema_def = SchemaDefinition(fields=fields)
        return super(SchemaMetaclass, cls).__new__(
            cls, clsname, bases, {**attribs, "_schema_definition": schema_def}
        )


SchemaVar = TypeVar("SchemaVar", bound="Schema")


class Schema(metaclass=SchemaMetaclass):
    _schema_definition: ClassVar[SchemaDefinition]

    def __init__(self, **kwargs) -> None:
        defined_fields = self._schema_definition.fields
        for k, v in kwargs.items():
            if k not in defined_fields:
                continue
            setattr(self, k, v)

    @classmethod
    def clean(
        cls: Type[SchemaVar], data: Any, context: Any = empty
    ) -> Union[SchemaVar, ValidationError]:
        result = clean(cls._schema_definition, data, context)
        if isinstance(result, ValidationError):
            return result
        else:
            return cls(**result)

    def serialize(self) -> Dict:
        return serialize(
            self._schema_definition,
            {
                n: getattr(self, n)
                for n in self._schema_definition.fields.keys()
            },
        )
