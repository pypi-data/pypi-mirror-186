from typing import List, Optional, Set, Type, TypeVar

import attr

from cleanchausie.fields import (
    Error,
    Field,
    Omittable,
    PolySchemaMapping,
    Required,
)
from cleanchausie.schema import Schema, field_def_from_annotation
from cleanchausie.schema_definition import (
    SchemaDefinition,
    make_clean_with_factory,
)


def convert_attrib_to_field(attrib: attr.Attribute) -> Field:
    """Convert attr Attribute to cleanchausie Field."""
    if attrib.type:
        field = field_def_from_annotation(attrib.type)
        assert field
    else:
        field = Field(
            validators=(),
            accepts=(),
            nullability=Required(),
            depends_on=(),
            serialize_to=None,
            serialize_func=lambda v: v,
        )

    if attrib.default:
        nullability = Omittable(omitted_value=attrib.default)
        field = attr.evolve(field, nullability=nullability)

    if attrib.validator:

        def _validate(value):
            try:
                # no ability to validate against other values on the
                # instance (since no instance exists yet), but should
                # support simple validation cases.
                assert attrib.validator  # for mypy
                attrib.validator(None, attrib, value)
                return value
            except Exception as e:
                return Error(msg=str(e))

        new_validators = (field.validators or ()) + (_validate,)
        field = attr.evolve(field, validators=new_validators)

    return field


def schema_def_from_attrs_class(
    attrs_class: Type, ignore_fields: Optional[Set[str]] = None
) -> SchemaDefinition:
    return SchemaDefinition(
        fields={
            attr_field.name: convert_attrib_to_field(attr_field)
            for attr_field in attr.fields(attrs_class)
            if (not ignore_fields or attr_field.name not in ignore_fields)
        }
    )


def schema_for_attrs_class(
    attrs_class: Type, ignore_fields: Optional[List[str]] = None
) -> Type[Schema]:
    schema_definition = schema_def_from_attrs_class(
        attrs_class=attrs_class, ignore_fields=set(ignore_fields or [])
    )
    return type(
        f"{attrs_class.__name__}Schema",
        (Schema,),
        schema_definition.fields,
    )


T = TypeVar("T", bound=attr.AttrsInstance)


def poly_schema_mapping_for_attrs(
    t: Type[T], public_type: str
) -> PolySchemaMapping[T]:
    return PolySchemaMapping(
        public_type=public_type,
        internal_type=t,
        serializer=attr.asdict,
        clean=make_clean_with_factory(schema_def_from_attrs_class(t), t),
    )
