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

from .error_cause import ErrorCause
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field
from typing import Optional
from typing import List

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class ExtendedError:
    """@dataclass ExtendedError The object used the describe an error, containing both human-readable and in a machine-readable information.

    Attributes:
        type(str):A URI reference, compliant with the standard EG error type format, which identifies the error type. It provides a machine-readable identifier for the error type. The error type will be aligned with the HTTP status code of the response. The URI can either be absolute or relative to the API's base URI. When dereferenced, it can also provide human-readable documentation for the error type. 

        detail(str):A human-readable explanation of the error, specific to this error occurrence.

        causes([ErrorCause]):An array of cause objects, that identify the specific causes of the error.
    """
    type: str = field(
        default_factory=lambda: require_value("type"),
        metadata=config(exclude=lambda f: f is None)
    )
    detail: str = field(
        default_factory=lambda: require_value("detail"),
        metadata=config(exclude=lambda f: f is None)
    )
    causes: Optional[List[ErrorCause]] = field(default=None, metadata=config(exclude=lambda f: f is None))



