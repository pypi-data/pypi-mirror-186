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

from .amount import Amount
from .order_purchase_update_request import OrderPurchaseUpdateRequest
from datetime import datetime
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class RefundUpdate(OrderPurchaseUpdateRequest):
    """@dataclass RefundUpdate

    Attributes:
        acquirer_reference_number(str):A unique number that tags a credit or debit card transaction when it goes from the merchant's bank through to the cardholder's bank.

        refund_deposit_timestamp(datetime):Date and time when the refund was deposited to the original form of payment.

        refund_settlement_timestamp(datetime):Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has settled at the participating financial institutions.

        settlement_id(str):Unique settlement identifier generated for a previously submitted payment refund.

        refund_amount(Amount):
    """
    acquirer_reference_number: str = field(
        default_factory=lambda: require_value("acquirer_reference_number"),
        metadata=config(exclude=lambda f: f is None)
    )
    refund_deposit_timestamp: datetime = field(
        default_factory=lambda: require_value("refund_deposit_timestamp"),
        metadata=config(exclude=lambda f: f is None)
    )
    refund_settlement_timestamp: datetime = field(
        default_factory=lambda: require_value("refund_settlement_timestamp"),
        metadata=config(exclude=lambda f: f is None)
    )
    settlement_id: str = field(
        default_factory=lambda: require_value("settlement_id"),
        metadata=config(exclude=lambda f: f is None)
    )
    refund_amount: Amount = field(
        default_factory=lambda: require_value("refund_amount"),
        metadata=config(exclude=lambda f: f is None)
    )



