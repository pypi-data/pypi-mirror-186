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


class TelephoneType(Enum):
    """Enum TelephoneType:
    Attributes:
        HOME(Enum): Classification of the phone (e.g. `Home`, `Mobile`). 
        MOBILE(Enum): Classification of the phone (e.g. `Home`, `Mobile`). 
        BUSINESS(Enum): Classification of the phone (e.g. `Home`, `Mobile`). 
        FAX(Enum): Classification of the phone (e.g. `Home`, `Mobile`). 
        OTHER(Enum): Classification of the phone (e.g. `Home`, `Mobile`). 
    """
    HOME = "HOME"
    MOBILE = "MOBILE"
    BUSINESS = "BUSINESS"
    FAX = "FAX"
    OTHER = "OTHER"


