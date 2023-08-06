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
from .telephone import Telephone
from datetime import datetime
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
class CreditCard(Payment):
    """@dataclass CreditCard

    Attributes:
        card_type(str):Type of card used for payment, (eg. `CREDIT`, `DEBIT`).

        card_number(str):All the digits (unencrypted) of the credit card number associated with the payment.

        expiry_date(datetime):Expiration date of the credit card used for payment.

        electronic_commerce_indicator(str):Electronic Commerce Indicator, a two or three digit number usually returned by a 3rd party payment processor in regards to the authentication used when gathering the cardholder's payment credentials.

        virtual_credit_card_flag(bool):A flag to indicate that the bank card being used for the charge is a virtual credit card.

        wallet_type(str):If a virtual/digital form of payment was used, the type of digital wallet should be specified here. Possible `wallet_type`'s include: `Google` or `ApplePay`.

        card_avs_response(str):A field used to confirm if the address provided at the time of purchase matches what the bank has on file for the Credit Card.

        card_cvv_response(str):A field used to confirm the Card Verification Value on the Credit Card matches the Credit Card used at the time of purchase.

        telephones([Telephone]):Telephone(s) associated with card holder and credit card.

        merchant_order_code(str):Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
    """
    card_type: str = field(
        default_factory=lambda: require_value("card_type"),
        metadata=config(exclude=lambda f: f is None)
    )
    card_number: str = field(
        default_factory=lambda: require_value("card_number"),
        metadata=config(exclude=lambda f: f is None)
    )
    card_avs_response: str = field(
        default_factory=lambda: require_value("card_avs_response"),
        metadata=config(exclude=lambda f: f is None)
    )
    card_cvv_response: str = field(
        default_factory=lambda: require_value("card_cvv_response"),
        metadata=config(exclude=lambda f: f is None)
    )
    telephones: List[Telephone] = field(
        default_factory=lambda: require_value("telephones"),
        metadata=config(exclude=lambda f: f is None)
    )
    expiry_date: Optional[datetime] = field(default=None, metadata=config(exclude=lambda f: f is None))
    electronic_commerce_indicator: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    virtual_credit_card_flag: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))
    wallet_type: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    merchant_order_code: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))



