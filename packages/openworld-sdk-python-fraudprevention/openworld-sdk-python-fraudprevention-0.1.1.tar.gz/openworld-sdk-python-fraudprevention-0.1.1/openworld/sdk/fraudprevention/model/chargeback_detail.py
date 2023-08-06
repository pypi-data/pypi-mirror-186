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
from typing import Union
from typing import Optional

def require_value(var: str):
    raise TypeError(f'None value not allowed for attribute {var}!')


@dataclass_json
@dataclass
class ChargebackDetail:
    """@dataclass ChargebackDetail Details related to the chargeback.

    Attributes:
        chargeback_reason(str):Reason for chargeback which can be `Fraud` or `Non Fraud`.

        chargeback_amount(int, float):Chargeback amount received by the partner.

        currency_code(str):The 3-letter currency code defined in ISO 4217. https://www.currency-iso.org/dam/downloads/lists/list_one.xml.

        bank_reason_code(str):Unique code provided by the acquiring bank for the category of fraud.

        chargeback_reported_timestamp(datetime):Date and time when the chargeback was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    chargeback_reason: str = field(
        default_factory=lambda: require_value("chargeback_reason"),
        metadata=config(exclude=lambda f: f is None)
    )
    chargeback_amount: Union[Union[int, float]] = field(
        default_factory=lambda: require_value("chargeback_amount"),
        metadata=config(exclude=lambda f: f is None)
    )
    currency_code: str = field(
        default_factory=lambda: require_value("currency_code"),
        metadata=config(exclude=lambda f: f is None)
    )
    bank_reason_code: Optional[str] = field(default=None, metadata=config(exclude=lambda f: f is None))
    chargeback_reported_timestamp: Optional[datetime] = field(default=None, metadata=config(exclude=lambda f: f is None))



