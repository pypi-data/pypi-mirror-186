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

from .air_segment import AirSegment
from .travel_product import TravelProduct
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
class Air(TravelProduct):
    """@dataclass Air

    Attributes:
        departure_time(datetime):Local date and time of departure from original departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

        arrival_time(datetime):Local date and time of arrival to final destination location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

        air_segments([AirSegment]):Additional airline and flight details for each of the trip segments.

        flight_type(str):Identifies the type of air trip based on the air destinations.

        passenger_name_record(str):Airline booking confirmation code for the trip.

        global_distribution_system_type(str):Associated with Passenger Name Record (PNR).
    """
    departure_time: datetime = field(
        default_factory=lambda: require_value("departure_time"),
        metadata=config(exclude=lambda f: f is None)
    )
    arrival_time: datetime = field(
        default_factory=lambda: require_value("arrival_time"),
        metadata=config(exclude=lambda f: f is None)
    )
    air_segments: List[AirSegment] = field(
        default_factory=lambda: require_value("air_segments"),
        metadata=config(exclude=lambda f: f is None)
    )
    flight_type: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    passenger_name_record: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    global_distribution_system_type: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))



