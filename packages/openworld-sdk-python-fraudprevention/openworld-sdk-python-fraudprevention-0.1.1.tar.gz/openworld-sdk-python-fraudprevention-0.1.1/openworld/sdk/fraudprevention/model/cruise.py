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
class Cruise(TravelProduct):
    """@dataclass Cruise

    Attributes:
        departure_time(datetime):Local date and time of departure from original departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

        arrival_time(datetime):Local date and time of arrival from original arrival location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

        embarkation_port(str):Location from where cruise will depart.

        disembarkation_port(str):The cruise's final destination.

        ship_name(str):Name of the cruise ship.
    """
    departure_time: datetime = field(
        default_factory=lambda: require_value("departure_time"),
        metadata=config(exclude=lambda f: f is None)
    )
    arrival_time: datetime = field(
        default_factory=lambda: require_value("arrival_time"),
        metadata=config(exclude=lambda f: f is None)
    )
    embarkation_port: str = field(
        default_factory=lambda: require_value("embarkation_port"),
        metadata=config(exclude=lambda f: f is None)
    )
    disembarkation_port: str = field(
        default_factory=lambda: require_value("disembarkation_port"),
        metadata=config(exclude=lambda f: f is None)
    )
    ship_name: str = field(
        default_factory=lambda: require_value("ship_name"),
        metadata=config(exclude=lambda f: f is None)
    )



