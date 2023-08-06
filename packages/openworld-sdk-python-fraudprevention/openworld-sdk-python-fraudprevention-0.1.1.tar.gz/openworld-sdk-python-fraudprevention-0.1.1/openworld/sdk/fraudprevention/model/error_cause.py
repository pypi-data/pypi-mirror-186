# Copyright 2022 Expedia, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field
from typing import Optional

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class ErrorCause:
    """@dataclass ErrorCause The object used to describe a cause for an error, containing both human-readable and in a machine-readable information.

    Attributes:
        type(str):A URI reference, compliant with the standard EG error type format, which identifies the cause type. It provides a machine-readable identifier for the cause type. The cause type will be aligned with the error type. The URI can either be absolute or relative to the API's base URI. When dereferenced, it provides human-readable documentation for the cause type. 

        detail(str):A human-readable explanation of the cause, specific to this cause occurrence.

        location(str):The location of the element in the request that identifies this specific cause. When specified, the `name` will be specified and when applicable, the `value` as well. Can be one of: * `HEADER` - When an error has been identified in one of the request headers. * `PATH` - When an error has been identified in one of the path parameters. * `QUERY` - When an error has been identified in one of the query parameters. * `BODY` - When an error has been identified in the request body. 

        name(str):The name of the element for this cause. When specified, the `location` will be specified and when applicable, the `value` as well. This name is a function of the value of the `location` property:   * When the `location` is set to `HEADER`, this will be the name of the request header (e.g. `Content-Type`).   * When the `location` is set to `PATH`, this will be the name of the path parameter (e.g. in a path defined as `/users/{user_id}`, the value would be `user_id`).   * When the `location` is set to `QUERY`, this will be the name of the query string parameter (e.g. `offset`).   * When the `location` is set to `BODY`, this will one of the field names specified in the body of the request.     * For a top level field, it should only be set to the field name (e.g. `firstName`).     * For a field in a nested object, it may contain the path to reach the field (e.g. `address.city`).     * For a field in an object part of collection, it may contain the index in the collection (e.g. `permissions[0].name`). 

        value(str):A string representation of the erroneous value of the element identified in `name`, perceived to be the cause of the error. When specified, the `location` and `name` should be specified as well. This value may be omitted in cases where it cannot be provided (e.g. missing require field), or the erroneous value cannot be represented as a string. 
    """
    type: str = field(
        default_factory=lambda: require_value("type"),
        metadata=config(exclude=lambda f: f is None)
    )
    detail: str = field(
        default_factory=lambda: require_value("detail"),
        metadata=config(exclude=lambda f: f is None)
    )
    location: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    name: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    value: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))



