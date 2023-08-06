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

from .fraud_decision import FraudDecision
from .error_detail import ErrorDetail
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field
from typing import Optional

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class OrderPurchaseScreenResponse:
    """@dataclass OrderPurchaseScreenResponse 

    Attributes:
        risk_id(str):

        decision(FraudDecision):

        error_detail(ErrorDetail):
    """
    risk_id: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    decision: Optional[FraudDecision] = field(default=None, metadata=config(exclude=lambda f: f is None))
    error_detail: Optional[ErrorDetail] = field(default=None, metadata=config(exclude=lambda f: f is None))



