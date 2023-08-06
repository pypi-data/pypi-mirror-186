# CleanChausie

CleanChausie is a data validation and transformation library for Python. It is a successor to CleanCat.

*Interested in working on projects like this? [`Close`](https://close.com) is looking for [great engineers](https://jobs.close.com) to join our team.*

Key features:

- Operate on/with type-checked objects that have good IDE/autocomplete support
- Annotation-based declarations for simple fields
- Composable/reusable fields and field validation logic
- Support (but not require) passing around a context (to avoid global state)
  - Context pattern is compatible with explicit sqlalchemy-based session management. i.e. pass in a session when validating
- Cleanly support intra-schema field dependencies (i.e. one field can depend on the validated value of another)
- Explicit nullability/omission parameters
- Errors returned for multiple fields at a time, with field attribution

## Installation

CleanChausie requires Python 3.8+.
To install, run `python3 -m pip install cleanchausie`.

## CleanChausie by example

### A basic example in Flask

This shows:

- Annotation-based declarations for simple fields.
- Type-checked objects (successful validation results in initialized instances of the schema)

```python
from typing import List
from cleanchausie.fields import (
  EmailField, ListField, URLField, ValidationError, field
)
from cleanchausie.schema import Schema
from flask import app, request, jsonify

class JobApplication(Schema):
  first_name: str
  last_name: str
  email: str = field(EmailField())
  urls: List[str] = field(ListField(URLField(default_scheme='http://')))

@app.route('/job_application', methods=['POST'])
def test_view():
  result = JobApplication.clean(request.json)
  if isinstance(result, ValidationError):
    return jsonify({'errors': [{'msg': e.msg, 'field': e.field} for e in result.errors] }), 400

  # Now "result" has the validated data, in the form of a `JobApplication` instance.
  assert isinstance(result, JobApplication)
  name = f'{result.first_name} {result.last_name}'
```

### Errors (per-field, and all at once)

"Expected" errors (as a result of validation not passing) in CleanChausie
aren't handled with exceptions, they're _returned_. This gives us a few things:

- We can easily detect when our _validation routine_ isn't working how it's
  expected to (because exceptions are the result of _unexpected_ scenarios, and
  _aren't_ used for control flow)
- We can easily return structured information about these errors (like which
  field they're for)
- We can easily handle multiple errors in the same round trip, returned at the
  same time.

Errors are returned as a flat list, which simplifies handling _nested_ fields.
Each `Error` has a `field` tuple, which allows individual errors to reference
fields deeply nested inside of embedded objects or lists.

Let's start with a simple example:

```python
from cleanchausie.fields import Error, ValidationError
from cleanchausie.schema import Schema

class PerFieldErrorExampleSchema(Schema):
  first_name: str
  last_name: str

result = PerFieldErrorExampleSchema.clean({})
assert isinstance(result, ValidationError)
assert result.errors == [
  Error(msg='This field is required.', field=('last_name',)),
  Error(msg='This field is required.', field=('first_name',))
]
```

Now let's add some nesting:

```python
from cleanchausie.fields import (
  field, ListField, NestedField, ValidationError, Error
)
from cleanchausie.schema import Schema

class PhoneSchema(Schema):
  country_code: str
  number: str

class AddressSchema(Schema):
  street_name: str
  street_number: str
  zip: str

class UserSchema(Schema):
  email: str
  phone = field(NestedField(PhoneSchema))
  addresses = field(ListField(NestedField(AddressSchema)))

result = UserSchema.clean(
  {
    "phone": {"number": "1234567890"},
    "addresses": [{"street_name": "High St", "street_number": "1337"}],
  }
)
assert isinstance(result, ValidationError)
assert sorted(result.errors, key=lambda e: e.field) == [
  Error(msg="This field is required.", field=("addresses", 0, "zip")),
  Error(msg="This field is required.", field=("email",)),
  Error(msg="This field is required.", field=("phone", "country_code")),
]
```

### Explicit nullability

Nullability is explicit, and CleanChausie differentiates between:

- value is required and non-nullable
- value is required and nullable (if `None` is explicitly passed)
- omittable (expressed as an `omitted` constant)
- omittable, defaulting to a specific value

These variants can either be expressed explicitly, or CleanChausie will
define them automatically to match a Schema's type annotations.

```python
from typing import Optional, Union
from cleanchausie.consts import OMITTED
from cleanchausie.fields import field, StrField, Omittable, Required
from cleanchausie.schema import Schema

# auto define fields based on annotations
class NullabilityExample(Schema):
  nonnull_required: str
  nullable_required: Optional[str]
  nonnull_omittable: Union[str, OMITTED]
  nullable_omittable: Optional[Union[str, OMITTED]]

# or define the same fields explicitly
class NullabilityExplicitExample(Schema):
  nonnull_required = field(StrField())
  nullable_required = field(StrField(), nullability=Required(allow_none=True))
  nonnull_omittable = field(StrField(), nullability=Omittable(allow_none=False))
  nullable_omittable = field(StrField(), nullability=Omittable())
```

### Composable/Reusable fields

```python
from cleanchausie.fields import field, StrField, IntField
from cleanchausie.schema import Schema

@field(parents=StrField())
def name_field(value: str) -> str:
  return value.strip()

age_field = IntField(min_value=0)
score_field = IntField(min_value=0, max_value=100)

class ReusableFieldsExampleSchema(Schema):
  first_name = name_field
  age = age_field
  score = score_field
```

### Context support

CleanChausie supports passing in a _context_ during validation. This is
commonly useful for validation-important information or implementation details
that aren't _really_ part of the validated data and shouldn't be serialized as
a field.

For example, a database `session` often has a short lifecycle and should
be discarded after it's been used. If this was passed in as a field, a
reference would stick around on the validated schema. If we're just trying to
be explicit about session management, we should pass it in using a context
instead:

```python
import attrs
from cleanchausie.fields import field, StrField
from cleanchausie.schema import Schema

class MyModel:  # some ORM model
  id: str
  created_by_id: str  # User id

@attrs.frozen
class Context:
  authenticated_user: 'User'  # the User making a request
  session: 'Session'  # active ORM Session

class ContextExampleSchema(Schema):
  @field(parents=StrField(), accepts=("id",))
  def obj(self, value: str, context: Context) -> MyModel:
    # in real usage this might look more like:
    #   context.session
    #     .query(MyModel)
    #     .filter(MyModel.created_by_id == authenticated_user.id)
    #     .filter(MyModel.id == value)
    return context.session.find_by_user_and_id(
      value, context.authenticated_user.id
    )

with atomic() as session:
  result = ContextExampleSchema.clean(
    data={'id': 'mymodel_primarykey'},
    context=Context(authenticated_user=EXAMPLE_USER, session=session)
  )
assert isinstance(result, ContextExampleSchema)
assert isinstance(result.obj, MyModel)
```

### Intra-schema field dependencies

Fields can depend on each other! This is common in a few real-life use cases:

- An object can have an owning user/organization, which we might want to fetch
  first and reference while validating other fields
- We might want to automatically _derive_ a field's value based on other
  required values
- We might want to force field evaluation order to put the most expensive
  checks last

The semantics here is actually pretty straightforward! All you have to do when
defining a field is add an argument with a name matching another field. When
validating, CleanChausie will first validate the other field, then pass the
resulting value into subsequent fields that depend on them. For example:

```python
from cleanchausie.fields import field
from cleanchausie.schema import Schema

class DependencyExampleSchema(Schema):
  a: str
  b: str
  
  @field()
  def a_and_b(self, a: str, b: str) -> str:
    return f'{a}::{b}'


result = DependencyExampleSchema.clean(
  data={'a': 'foo', 'b': 'bar'},
)
assert isinstance(result, DependencyExampleSchema)
assert result.a_and_b == 'foo::bar'
```

Or we can write fields that both accept a value, and depend on the
already-valid values from other fields:

```python
import attr
from cleanchausie.fields import field, StrField
from cleanchausie.schema import Schema

@attr.frozen
class B:
  val: str

class DependencyExample2Schema(Schema):
  a: str

  @field(parents=StrField())
  def b(self, value: str) -> B:
    return B(val=value)

  @field()
  def a_and_b(self, a: str, b: B) -> str:
    return f"{a}::{b.val}"
```

## Release process

- Make sure to thoroughly review and test the code changes.
- Prepare for a new release
  - Update the package version within `cleanchausie/__init__.py`.
  - Add a changelog entry for the new version.
  - Merge to master
- Dispatch a new "build and release" workflow action within the github actions tab.

The resulting workflow will build and publish the new version to PyPi.
