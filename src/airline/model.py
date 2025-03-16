import dataclasses
from typing import Dict, Any, Optional

from pkg.json_object import JSONObject

ID = "ID"
TYPE = "Type"
COMPANY_NAME = "Company Name"
COUNTRY = "Country"
IATA_CODE = "IATA Code"


@dataclasses.dataclass
class Airline(JSONObject):
    airline_id: str
    airline_type: str
    company_name: str
    country: str
    iata_code: str

    def to_json(self) -> Dict[str, Any]:
        return {
            ID: self.airline_id,
            TYPE: self.airline_type,
            COMPANY_NAME: self.company_name,
            COUNTRY: self.country,
            IATA_CODE: self.iata_code
        }

    @classmethod
    def from_json(cls, json: Dict[str, Any]) -> 'Airline':
        if not json.get(ID):
            raise AirlineInvalidError("Airline ID is required.")
        if not json.get(ID).isdigit():
            raise AirlineInvalidError("Airline ID must be a number.")
        return cls(
            airline_id=json.get(ID),
            airline_type=json.get(TYPE, ""),
            company_name=json.get(COMPANY_NAME, ""),
            country=json.get(COUNTRY, ""),
            iata_code=json.get(IATA_CODE, "")
        )

@dataclasses.dataclass
class AirlineUpdateRequest(JSONObject):
    airline_id: str
    airline_type: Optional[str] = None
    company_name: Optional[str] = None
    country: Optional[str] = None
    iata_code: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        return {
            ID: self.airline_id,
            TYPE: self.airline_type,
            COMPANY_NAME: self.company_name,
            COUNTRY: self.country,
            IATA_CODE: self.iata_code
        }

    @classmethod
    def from_json(cls, json: Dict[str, Any]) -> 'AirlineUpdateRequest':
        if not json.get(ID):
            raise AirlineInvalidError("Airline ID is required.")
        if not json.get(ID).isdigit():
            raise AirlineInvalidError("Airline ID must be a number.")
        return cls(
            airline_id=json.get(ID),
            airline_type=json.get(TYPE),
            company_name=json.get(COMPANY_NAME),
            country=json.get(COUNTRY),
            iata_code=json.get(IATA_CODE)
        )

class AirlineInvalidError(Exception):
    pass
