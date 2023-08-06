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

from .transaction_details import TransactionDetails
from .order_purchase_transaction import OrderPurchaseTransaction
from .customer_account import CustomerAccount
from .device_details import DeviceDetails
from .site_info import SiteInfo
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field
from typing import Optional

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class OrderPurchaseTransaction:
    """@dataclass OrderPurchaseTransaction 

    Attributes:
        site_info(SiteInfo):

        device_details(DeviceDetails):

        customer_account(CustomerAccount):

        transaction_details(TransactionDetails):

        bypass_risk_flag(bool):A flag to indicate whether the client is ignoring the decision by Trust validation and proceeds to process the even in-case the outcome is ‘Reject’ or ‘Review’.
    """
    site_info: SiteInfo = field(
        default_factory=lambda: require_value("site_info"),
        metadata=config(exclude=lambda f: f is None)
    )
    device_details: DeviceDetails = field(
        default_factory=lambda: require_value("device_details"),
        metadata=config(exclude=lambda f: f is None)
    )
    customer_account: CustomerAccount = field(
        default_factory=lambda: require_value("customer_account"),
        metadata=config(exclude=lambda f: f is None)
    )
    transaction_details: TransactionDetails = field(
        default_factory=lambda: require_value("transaction_details"),
        metadata=config(exclude=lambda f: f is None)
    )
    bypass_risk_flag: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))



