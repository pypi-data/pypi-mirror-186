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

from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses import field
from typing import Optional

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class Address:
    """@dataclass Address 

    Attributes:
        address_line1(str):Address line 1 of the address provided.

        city(str):City of the address provided.

        state(str):The two-characters ISO code for the state or province of the address.

        zip_code(str):Zip code of the address provided.

        country_code(str):ISO alpha-3 country code of the address provided.

        address_type(str):

        address_line2(str):Address line 2 of the address provided.
    """
    address_line1: str = field(
        default_factory=lambda: require_value("address_line1"),
        metadata=config(exclude=lambda f: f is None)
    )
    city: str = field(
        default_factory=lambda: require_value("city"),
        metadata=config(exclude=lambda f: f is None)
    )
    state: str = field(
        default_factory=lambda: require_value("state"),
        metadata=config(exclude=lambda f: f is None)
    )
    zip_code: str = field(
        default_factory=lambda: require_value("zip_code"),
        metadata=config(exclude=lambda f: f is None)
    )
    country_code: str = field(
        default_factory=lambda: require_value("country_code"),
        metadata=config(exclude=lambda f: f is None)
    )
    address_type: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    address_line2: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))



