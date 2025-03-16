import dataclasses
from typing import Dict, Any, Optional

from pkg.json_object import JSONObject


ID = "ID"
TYPE = "Type"
NAME = "Name"
ADDRESS = "Address Line 1"
CITY = "City"
STATE = "State"
COUNTRY = "Country"
PHONE = "Phone Number"


@dataclasses.dataclass
class Client(JSONObject):
    client_id: str
    client_type: str
    name: str
    address_line_1: str
    city: str
    state: str
    country: str
    phone: str

    def to_json(self) -> Dict[str, Any]:
        return {
            ID: self.client_id,
            TYPE: self.client_type,
            NAME: self.name,
            ADDRESS: self.address_line_1,
            CITY: self.city,
            STATE: self.state,
            COUNTRY: self.country,
            PHONE: self.phone
        }

    @classmethod
    def from_json(cls, json: Dict[str, Any]) -> 'Client':
        if not json.get(ID):
            raise ClientInvalidError("Client ID is required.")
        if not json.get(ID).isdigit():
            raise ClientInvalidError("Client ID must be a number.")
        return cls(
            client_id=json.get(ID),
            client_type=json.get(TYPE, ""),
            name=json.get(NAME, ""),
            address_line_1=json.get(ADDRESS, ""),
            city=json.get(CITY, ""),
            state=json.get(STATE, ""),
            country=json.get(COUNTRY, ""),
            phone=json.get(PHONE, "")
        )

@dataclasses.dataclass
class ClientUpdateRequest(JSONObject):
    client_id: str
    client_type: Optional[str] = None
    name: Optional[str] = None
    address_line_1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    phone: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        return {
            ID: self.client_id,
            TYPE: self.client_type,
            NAME: self.name,
            ADDRESS: self.address_line_1,
            CITY: self.city,
            STATE: self.state,
            COUNTRY: self.country,
            PHONE: self.phone
        }

    @classmethod
    def from_json(cls, json: Dict[str, Any]) -> 'ClientUpdateRequest':
        if not json.get(ID):
            raise ClientInvalidError("Client ID is required.")
        if not json.get(ID).isdigit():
            raise ClientInvalidError("Client ID must be a number.")
        return cls(
            client_id=json.get(ID),
            client_type=json.get(TYPE),
            name=json.get(NAME),
            address_line_1=json.get(ADDRESS),
            city=json.get(CITY),
            state=json.get(STATE),
            country=json.get(COUNTRY),
            phone=json.get(PHONE)
        )


class ClientInvalidError(Exception):
    pass
