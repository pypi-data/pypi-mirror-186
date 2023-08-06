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
class Name:
    """@dataclass Name Group of attributes intended to hold information about a customer or traveler's name for the order.

    Attributes:
        last_name(str):Surname, or last name, of the person.

        first_name(str):Given, or first name, of the person.

        middle_name(str):Middle name of the person.

        title(str):Title of the person for name (e.g. Mr., Ms. etc).

        suffix(str):Generational designations (e.g. Sr, Jr, III) or values that indicate the individual holds a position, educational degree, accreditation, office, or honor (e.g. PhD, CCNA, OBE).

        full_name(str):Full name of the person that includes title, first_name, middle_name, last_name, suffix.
    """
    last_name: str = field(
        default_factory=lambda: require_value("last_name"),
        metadata=config(exclude=lambda f: f is None)
    )
    first_name: str = field(
        default_factory=lambda: require_value("first_name"),
        metadata=config(exclude=lambda f: f is None)
    )
    middle_name: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    title: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    suffix: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    full_name: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))



