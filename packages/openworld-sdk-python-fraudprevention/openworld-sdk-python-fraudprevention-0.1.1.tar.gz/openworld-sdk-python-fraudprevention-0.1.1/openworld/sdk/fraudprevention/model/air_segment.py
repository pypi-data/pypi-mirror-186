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
class AirSegment:
    """@dataclass AirSegment 

    Attributes:
        airline_code(str):Airline code of the trip segment

        departure_airport_code(str):Departure airport of the trip segment

        arrival_airport_code(str):Arrival airport of the trip segment

        departure_time(datetime):Local date and time of departure from departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

        arrival_time(datetime):Local date and time of arrival to destination location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    airline_code: str = field(
        default_factory=lambda: require_value("airline_code"),
        metadata=config(exclude=lambda f: f is None)
    )
    departure_airport_code: str = field(
        default_factory=lambda: require_value("departure_airport_code"),
        metadata=config(exclude=lambda f: f is None)
    )
    arrival_airport_code: str = field(
        default_factory=lambda: require_value("arrival_airport_code"),
        metadata=config(exclude=lambda f: f is None)
    )
    departure_time: Optional[datetime] = field(default=None, metadata=config(exclude=lambda f: f is None))
    arrival_time: Optional[datetime] = field(default=None, metadata=config(exclude=lambda f: f is None))



