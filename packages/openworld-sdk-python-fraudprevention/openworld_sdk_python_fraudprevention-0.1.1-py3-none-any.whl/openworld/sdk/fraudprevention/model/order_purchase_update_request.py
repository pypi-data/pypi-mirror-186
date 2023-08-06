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

from .update_type import UpdateType
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class OrderPurchaseUpdateRequest:
    """@dataclass OrderPurchaseUpdateRequest 

    Attributes:
        type(UpdateType):

        risk_id(str):The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    type: UpdateType = field(
        default_factory=lambda: require_value("type"),
        metadata=config(exclude=lambda f: f is None)
    )
    risk_id: str = field(
        default_factory=lambda: require_value("risk_id"),
        metadata=config(exclude=lambda f: f is None)
    )



