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


class Status(Enum):
    """Enum Status:
    Attributes:
        COMPLETED(Enum): Defines the current state of the Order.
        CHANGE_COMPLETED(Enum): Defines the current state of the Order.
        CANCELLED(Enum): Defines the current state of the Order.
        FAILED(Enum): Defines the current state of the Order.
        CHANGE_FAILED(Enum): Defines the current state of the Order.
    """
    COMPLETED = "COMPLETED"
    CHANGE_COMPLETED = "CHANGE_COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    CHANGE_FAILED = "CHANGE_FAILED"


