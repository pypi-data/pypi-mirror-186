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

from .name import Name
from .telephone import Telephone
from datetime import datetime
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field
from typing import Union
from typing import Optional
from typing import List

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class Traveler:
    """@dataclass Traveler 

    Attributes:
        traveler_name(Name):

        email_address(str):Email address associated with the traveler as supplied by the partner system.

        telephones([Telephone]):

        primary(bool):Indicator for one of the travelers who is the primary traveler. One traveler in each itinerary item must be listed as primary. By default, for a single traveler this should be set to `true`.

        age(int, float):Age of the traveler.

        birth_date(datetime):Date of birth for traveler, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

        citizenship_country_code(str):The alpha-3 ISO country code of the traveler's nationality.

        traveler_id(str):A unique identifier for travelers in the transaction.
    """
    traveler_name: Name = field(
        default_factory=lambda: require_value("traveler_name"),
        metadata=config(exclude=lambda f: f is None)
    )
    email_address: str = field(
        default_factory=lambda: require_value("email_address"),
        metadata=config(exclude=lambda f: f is None)
    )
    telephones: List[Telephone] = field(
        default_factory=lambda: require_value("telephones"),
        metadata=config(exclude=lambda f: f is None)
    )
    primary: bool = field(
        default_factory=lambda: require_value("primary"),
        metadata=config(exclude=lambda f: f is None)
    )
    age: Optional[Union[int, float]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    birth_date: Optional[datetime] = field(default=None, metadata=config(exclude=lambda f: f is None))
    citizenship_country_code: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    traveler_id: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))



