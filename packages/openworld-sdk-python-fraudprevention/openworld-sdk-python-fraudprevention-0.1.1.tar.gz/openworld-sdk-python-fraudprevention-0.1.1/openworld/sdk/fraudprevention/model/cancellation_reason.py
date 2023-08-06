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
class CancellationReason:
    """@dataclass CancellationReason Reason of order update cancellation.

    Attributes:
        primary_reason_description(str):Primary cancellation reason code. Required if `order_status = CANCELLED`.

        primary_reason_code(str):Primary cancellation reason code.

        sub_reason_code(str):Substitute cancellation reason code.

        sub_reason_description(str):Substitute cancellation reason description.
    """
    primary_reason_description: str = field(
        default_factory=lambda: require_value("primary_reason_description"),
        metadata=config(exclude=lambda f: f is None)
    )
    primary_reason_code: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    sub_reason_code: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    sub_reason_description: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))



