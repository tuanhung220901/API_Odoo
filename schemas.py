from enum import Enum
from turtle import done
from pydantic import BaseModel


class UpdateSchema(BaseModel):
    x_name: str
    x_studio_s_in_thoi: str
    x_studio_a_ch: str


class StateEnum(str, Enum):
    assigned = "assigned"
    done = "done"
    cancel = "cancel"
    confirmed = "confirmed"
    draft = "draft"