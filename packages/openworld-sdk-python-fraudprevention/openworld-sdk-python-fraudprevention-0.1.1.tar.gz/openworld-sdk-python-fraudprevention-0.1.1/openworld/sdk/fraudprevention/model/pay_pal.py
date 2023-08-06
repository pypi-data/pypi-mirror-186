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

from .payment import Payment
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field
from typing import Optional

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class PayPal(Payment):
    """@dataclass PayPal

    Attributes:
        payer_id(str):Unique PayPal Customer Account identification number.

        transaction_id(str):Unique transaction number to identify Auth calls at PayPal.

        merchant_order_code(str):Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
    """
    payer_id: str = field(
        default_factory=lambda: require_value("payer_id"),
        metadata=config(exclude=lambda f: f is None)
    )
    transaction_id: str = field(
        default_factory=lambda: require_value("transaction_id"),
        metadata=config(exclude=lambda f: f is None)
    )
    merchant_order_code: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))



