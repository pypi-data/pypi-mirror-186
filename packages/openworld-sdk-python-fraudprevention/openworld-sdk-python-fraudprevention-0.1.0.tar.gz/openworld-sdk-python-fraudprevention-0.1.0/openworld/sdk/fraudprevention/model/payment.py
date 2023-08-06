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
from .payment_method import PaymentMethod
from .payment_three_ds_criteria import PaymentThreeDSCriteria
from .address import Address
from .payment_reason import PaymentReason
from .name import Name
from .payment import Payment
from .operations import Operations
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field
from typing import Union
from typing import Optional

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class Payment:
    """@dataclass Payment 

    Attributes:
        brand(str):Payment brand used for payment on this transaction.

        method(PaymentMethod):

        billing_name(Name):

        reason(PaymentReason):

        billing_address(Address):

        billing_email_address(str):Email address associated with the payment.

        authorized_amount(Amount):

        verified_amount(Amount):

        three_digits_secure_criteria(PaymentThreeDSCriteria):

        operations(Operations):

        total_refund_amount(int, float):Total amount refunded towards the transaction.
    """
    brand: str = field(
        default_factory=lambda: require_value("brand"),
        metadata=config(exclude=lambda f: f is None)
    )
    method: PaymentMethod = field(
        default_factory=lambda: require_value("method"),
        metadata=config(exclude=lambda f: f is None)
    )
    billing_name: Name = field(
        default_factory=lambda: require_value("billing_name"),
        metadata=config(exclude=lambda f: f is None)
    )
    reason: Optional[PaymentReason] = field(default=None, metadata=config(exclude=lambda f: f is None))
    billing_address: Optional[Address] = field(default=None, metadata=config(exclude=lambda f: f is None))
    billing_email_address: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    authorized_amount: Optional[Amount] = field(default=None, metadata=config(exclude=lambda f: f is None))
    verified_amount: Optional[Amount] = field(default=None, metadata=config(exclude=lambda f: f is None))
    three_digits_secure_criteria: Optional[PaymentThreeDSCriteria] = field(default=None, metadata=config(exclude=lambda f: f is None))
    operations: Optional[Operations] = field(default=None, metadata=config(exclude=lambda f: f is None))
    total_refund_amount: Optional[Union[Union[int, float]]] = field(default=None, metadata=config(exclude=lambda f: f is None))



