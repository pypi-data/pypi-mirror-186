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


from enum import Enum


class PaymentReason(Enum):
    """Enum PaymentReason:
    Attributes:
        FULL(Enum): The reason of payment. Possible values: - `FULL` - If the amount is paid i full for the order - `DEPOSIT` - The initial payment. Amount to be paid up front. - `SCHEDULED` - The amount to be payment based on a schedule for the remaining portion of the booking amount. - `SUBSEQUENT` - An additional amount paid that was not originally scheduled. - `DEFERRED` 
        DEPOSIT(Enum): The reason of payment. Possible values: - `FULL` - If the amount is paid i full for the order - `DEPOSIT` - The initial payment. Amount to be paid up front. - `SCHEDULED` - The amount to be payment based on a schedule for the remaining portion of the booking amount. - `SUBSEQUENT` - An additional amount paid that was not originally scheduled. - `DEFERRED` 
        SCHEDULED(Enum): The reason of payment. Possible values: - `FULL` - If the amount is paid i full for the order - `DEPOSIT` - The initial payment. Amount to be paid up front. - `SCHEDULED` - The amount to be payment based on a schedule for the remaining portion of the booking amount. - `SUBSEQUENT` - An additional amount paid that was not originally scheduled. - `DEFERRED` 
        SUBSEQUENT(Enum): The reason of payment. Possible values: - `FULL` - If the amount is paid i full for the order - `DEPOSIT` - The initial payment. Amount to be paid up front. - `SCHEDULED` - The amount to be payment based on a schedule for the remaining portion of the booking amount. - `SUBSEQUENT` - An additional amount paid that was not originally scheduled. - `DEFERRED` 
        DEFERRED(Enum): The reason of payment. Possible values: - `FULL` - If the amount is paid i full for the order - `DEPOSIT` - The initial payment. Amount to be paid up front. - `SCHEDULED` - The amount to be payment based on a schedule for the remaining portion of the booking amount. - `SUBSEQUENT` - An additional amount paid that was not originally scheduled. - `DEFERRED` 
    """
    FULL = "FULL"
    DEPOSIT = "DEPOSIT"
    SCHEDULED = "SCHEDULED"
    SUBSEQUENT = "SUBSEQUENT"
    DEFERRED = "DEFERRED"


