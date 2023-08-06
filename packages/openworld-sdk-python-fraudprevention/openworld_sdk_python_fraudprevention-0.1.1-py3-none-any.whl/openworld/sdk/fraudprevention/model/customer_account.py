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
from .name import Name
from .telephone import Telephone
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
class CustomerAccount:
    """@dataclass CustomerAccount 

    Attributes:
        account_type(str):Identifies if the customer account is known to the client. Possible values are:  -`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.  -`STANDARD` - Default account type. 

        name(Name):

        email_address(str):Email address for the account owner.

        user_id(str):Unique identifier assigned to the account owner by the partner. `user_id` is specific to the partner namespace

        telephones([Telephone]):

        address(Address):

        registered_time(datetime):The local date and time that the customer first registered on the client site, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    account_type: str = field(
        default_factory=lambda: require_value("account_type"),
        metadata=config(exclude=lambda f: f is None)
    )
    name: Name = field(
        default_factory=lambda: require_value("name"),
        metadata=config(exclude=lambda f: f is None)
    )
    email_address: str = field(
        default_factory=lambda: require_value("email_address"),
        metadata=config(exclude=lambda f: f is None)
    )
    user_id: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    telephones: Optional[List[Telephone]] = field(default=None, metadata=config(exclude=lambda f: f is None))
    address: Optional[Address] = field(default=None, metadata=config(exclude=lambda f: f is None))
    registered_time: Optional[datetime] = field(default=None, metadata=config(exclude=lambda f: f is None))



