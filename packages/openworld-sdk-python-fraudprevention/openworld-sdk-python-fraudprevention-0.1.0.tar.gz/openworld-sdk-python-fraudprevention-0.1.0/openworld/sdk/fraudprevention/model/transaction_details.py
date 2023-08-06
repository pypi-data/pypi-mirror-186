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
from .traveler import Traveler
from .payment import Payment
from .travel_product import TravelProduct
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
class TransactionDetails:
    """@dataclass TransactionDetails 

    Attributes:
        order_id(str):Unique identifier assigned to the order by the partner. `order_id` is specific to the partner namespace.

        current_order_status(str):Status of the order.

        order_type(str):Type of order. Possible `order_types`.  `CREATE` - Initial type of a brand new order.  `CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted for the initial booking with `order_type = CREATE`, but has now been modified and partner wishes to resubmit for Fraud screening then the `order_type = CHANGE`. Examples of changes that are supported are changes made to `check-in/checkout dates` or `price of a TravelProduct`. 

        travel_products([TravelProduct]):

        travelers([Traveler]):Individuals who are part of the travel party for the order. At minimum there must be at least `1` traveler.

        payments([Payment]):List of the form(s) of payment being used to purchase the order.  One or more forms of payment can be used within an order. Information gathered will be specific to the form of payment.

        credit_card_authentication_failure_count(int):Total authentication failure count for given credit card. Authentication failures happen when a cardholder enters their card information incorrectly.
    """
    order_id: str = field(
        default_factory=lambda: require_value("order_id"),
        metadata=config(exclude=lambda f: f is None)
    )
    current_order_status: str = field(
        default_factory=lambda: require_value("current_order_status"),
        metadata=config(exclude=lambda f: f is None)
    )
    order_type: str = field(
        default_factory=lambda: require_value("order_type"),
        metadata=config(exclude=lambda f: f is None)
    )
    travel_products: List[TravelProduct] = field(
        default_factory=lambda: require_value("travel_products"),
        metadata=config(exclude=lambda f: f is None)
    )
    travelers: List[Traveler] = field(
        default_factory=lambda: require_value("travelers"),
        metadata=config(exclude=lambda f: f is None)
    )
    payments: List[Payment] = field(
        default_factory=lambda: require_value("payments"),
        metadata=config(exclude=lambda f: f is None)
    )
    credit_card_authentication_failure_count: Optional[int] = field(default=None, metadata=config(exclude=lambda f: f is None))



