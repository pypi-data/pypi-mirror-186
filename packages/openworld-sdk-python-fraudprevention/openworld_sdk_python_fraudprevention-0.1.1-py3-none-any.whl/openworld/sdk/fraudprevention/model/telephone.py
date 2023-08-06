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

from .telephone_platform_type import TelephonePlatformType
from .telephone_type import TelephoneType
from datetime import datetime
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
class Telephone:
    """@dataclass Telephone Group of attributes intended to hold information about phone number associated with the transaction.  A user can have one to many phone numbers (home, work, mobile, etc.).

    Attributes:
        country_access_code(str):Numeric digit between 1 to 3 characters used to represent the country code for international dialing.  Does not include symbols, spaces, or leading zeros.

        area_code(str):A number prefixed to an individual telephone number: used in making long-distance calls.  Does not include symbols, spaces, or leading zeros.

        phone_number(str):A number that is dialed on a telephone, without the country or area codes, to reach a particular person, business, etc.  Does not include symbols, spaces, or leading zeros.

        type(TelephoneType):

        platform_type(TelephonePlatformType):

        full_phone_number(str):The concatenated countryAccessCode, areaCode, and phoneNumber with leading zeros from the original fields and symbols  (-,.+) removed.  It does not include a phone extension.

        extension_number(str):The number used to reach an individual once a phone connection is established.  Does not include symbols, spaces, or leading zeros.

        preference_rank(int, float):Ranking of order of user preference for contact via text (if type is Mobile) or voice.  `0` means no preference.  `1` is the primary phone, `2` is the secondary phone, etc.

        last_verified_timestamp(datetime):Local date and time user validated possession of their phone number via a text or voice multi factor authentication challenge, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

        verified_flag(bool):Flag indicating whether user passed validation of possession of their phone number via a text or voice multi factor authentication challenge.
    """
    country_access_code: str = field(
        default_factory=lambda: require_value("country_access_code"),
        metadata=config(exclude=lambda f: f is None)
    )
    area_code: str = field(
        default_factory=lambda: require_value("area_code"),
        metadata=config(exclude=lambda f: f is None)
    )
    phone_number: str = field(
        default_factory=lambda: require_value("phone_number"),
        metadata=config(exclude=lambda f: f is None)
    )
    type: Optional[TelephoneType] = field(default=None, metadata=config(exclude=lambda f: f is None))
    platform_type: Optional[TelephonePlatformType] = field(default=None, metadata=config(exclude=lambda f: f is None))
    full_phone_number: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    extension_number: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    preference_rank: Optional[Union[int, float]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    last_verified_timestamp: Optional[datetime] = field(default=None, metadata=config(exclude=lambda f: f is None))
    verified_flag: Optional[bool] = field(default=None, metadata=config(exclude=lambda f: f is None))



