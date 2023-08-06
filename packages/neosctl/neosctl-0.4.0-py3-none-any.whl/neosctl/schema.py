import configparser
import dataclasses
from enum import Enum
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import BaseModel


class FieldDataType(BaseModel):
    meta: Dict[str, Any]
    type: str


class FieldDefinition(BaseModel):
    name: str
    description: Optional[str] = None
    type: str
    primary: bool
    optional: bool
    data_type: FieldDataType


class DataProductCreate(BaseModel):
    engine: str
    fields: List[FieldDefinition]


class RegisterCore(BaseModel):
    partition: str
    name: str


class RemoveCore(BaseModel):
    urn: str


class Auth(BaseModel):
    access_token: str = ""
    expires_in: Optional[int] = None
    refresh_token: str = ""
    refresh_expires_in: Optional[int] = None


class OptionalProfile(BaseModel):
    gateway_api_url: str = ""
    registry_api_url: str = ""
    iam_api_url: str = ""
    storage_api_url: str = ""
    user: str = ""
    access_token: str = ""
    refresh_token: str = ""
    ignore_tls: bool = False


class Profile(BaseModel):
    gateway_api_url: str
    registry_api_url: str
    iam_api_url: str
    storage_api_url: str
    user: str
    access_token: str
    refresh_token: str
    ignore_tls: bool


class EffectEnum(Enum):
    allow: str = "allow"
    deny: str = "deny"


class Statement(BaseModel):
    sid: str
    principal: List[str]
    action: List[str]
    resource: List[str]
    condition: Optional[List[str]] = None
    effect: EffectEnum = EffectEnum.allow

    class Config:
        use_enum_values = True


class Statements(BaseModel):
    statements: List[Statement]


class Policy(BaseModel):
    version: str = "2022-10-01"
    statements: List[Statement]


class UserPolicy(BaseModel):
    user: str
    policy: Policy


@dataclasses.dataclass
class Common:
    gateway_api_url: str
    registry_api_url: str
    iam_api_url: str
    storage_api_url: str
    profile_name: str
    config: configparser.ConfigParser
    profile: Optional[Profile]

    def get_gateway_api_url(self):
        url = None
        if self.gateway_api_url:
            url = self.gateway_api_url
        elif self.profile and self.profile.gateway_api_url:
            url = self.profile.gateway_api_url
        return url

    def get_registry_api_url(self):
        url = None
        if self.registry_api_url:
            url = self.registry_api_url
        if self.profile and self.profile.registry_api_url:
            url = self.profile.registry_api_url
        return url

    def get_iam_api_url(self):
        url = None
        if self.iam_api_url:
            url = self.iam_api_url
        if self.profile and self.profile.iam_api_url:
            url = self.profile.iam_api_url
        return url

    def get_storage_api_url(self):
        url = None
        if self.storage_api_url:
            url = self.storage_api_url
        if self.profile and self.profile.storage_api_url:
            url = self.profile.storage_api_url
        return url
