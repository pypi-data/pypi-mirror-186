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
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field
from typing import List

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class TravelProduct:
    """@dataclass TravelProduct 

    Attributes:
        price(Amount):

        type(str):Type of product advertised on the website.

        inventory_type(str):Type of inventory.

        inventory_source(str):Identifies the business model through which the supply is being sold. Merchant/Agency.

        travelers_references([str]):List of travelerGuids who are part of the traveling party on the order for the product.
    """
    price: Amount = field(
        default_factory=lambda: require_value("price"),
        metadata=config(exclude=lambda f: f is None)
    )
    type: str = field(
        default_factory=lambda: require_value("type"),
        metadata=config(exclude=lambda f: f is None)
    )
    inventory_type: str = field(
        default_factory=lambda: require_value("inventory_type"),
        metadata=config(exclude=lambda f: f is None)
    )
    inventory_source: str = field(
        default_factory=lambda: require_value("inventory_source"),
        metadata=config(exclude=lambda f: f is None)
    )
    travelers_references: List[str] = field(
        default_factory=lambda: require_value("travelers_references"),
        metadata=config(exclude=lambda f: f is None)
    )



