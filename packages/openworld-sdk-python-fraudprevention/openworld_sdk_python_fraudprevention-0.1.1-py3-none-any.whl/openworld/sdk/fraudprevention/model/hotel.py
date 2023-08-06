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

from .address import Address
from .travel_product import TravelProduct
from datetime import datetime
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field
from typing import Optional

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class Hotel(TravelProduct):
    """@dataclass Hotel

    Attributes:
        hotel_id(str):Unique hotel identifier assigned by the partner.

        price_withheld(bool):Identifies if the product price was withheld from the customer during the booking process.

        hotel_name(str):Name of the hotel.

        room_count(int):Total number of rooms booked within the hotel product collection.

        address(Address):

        checkin_time(datetime):Local date and time of the hotel check-in, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

        checkout_time(datetime):Local date and time of the hotel check-out, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    hotel_id: str = field(
        default_factory=lambda: require_value("hotel_id"),
        metadata=config(exclude=lambda f: f is None)
    )
    hotel_name: str = field(
        default_factory=lambda: require_value("hotel_name"),
        metadata=config(exclude=lambda f: f is None)
    )
    address: Address = field(
        default_factory=lambda: require_value("address"),
        metadata=config(exclude=lambda f: f is None)
    )
    checkin_time: datetime = field(
        default_factory=lambda: require_value("checkin_time"),
        metadata=config(exclude=lambda f: f is None)
    )
    checkout_time: datetime = field(
        default_factory=lambda: require_value("checkout_time"),
        metadata=config(exclude=lambda f: f is None)
    )
    price_withheld: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))
    room_count: Optional[int] = field(default=None, metadata=config(exclude=lambda f: f is None))



