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

from .travel_product import TravelProduct
from datetime import datetime
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class Car(TravelProduct):
    """@dataclass Car

    Attributes:
        pick_up_location(str):Location where the automobile will be picked up.

        drop_off_location(str):Location at which the automobile will be returned.

        pickup_time(datetime):Local date and time the automobile will be picked-up, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

        return_time(datetime):Local date and time the automobile will be returned, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    pick_up_location: str = field(
        default_factory=lambda: require_value("pick_up_location"),
        metadata=config(exclude=lambda f: f is None)
    )
    drop_off_location: str = field(
        default_factory=lambda: require_value("drop_off_location"),
        metadata=config(exclude=lambda f: f is None)
    )
    pickup_time: datetime = field(
        default_factory=lambda: require_value("pickup_time"),
        metadata=config(exclude=lambda f: f is None)
    )
    return_time: datetime = field(
        default_factory=lambda: require_value("return_time"),
        metadata=config(exclude=lambda f: f is None)
    )



