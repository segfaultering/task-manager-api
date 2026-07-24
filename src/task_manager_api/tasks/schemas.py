import string
import datetime as dt
from typing import Annotated

from pydantic import BaseModel, Field, PositiveInt, AfterValidator, ConfigDict

from task_manager_api.tasks.models import Status


class Create(BaseModel): ...
class Update(BaseModel): ...
class Delete(BaseModel): ...
class Representation(BaseModel): ... 
class Response(BaseModel): ...


# Fields
Description = Annotated[
    str | None,
    Field(default=None, min_length=8)
]

Taskname = Annotated[
    str,
    Field(min_length=6, max_length=32),
    AfterValidator(is_valid_task_name)
]

TasknameNullable = Annotated[
    str | None,
    Field(default=None, min_length=6, max_length=32),
    AfterValidator(is_valid_task_name)
]
    

# Schemas 
class TaskCreate(Create):
    name: Taskname  
    description: Description 


class TaskUpdate(Update):
    name: TasknameNullable 
    description: Description
    stat: Status | None = Field(default=None)


class TaskRepr(Representation):
    id: PositiveInt 
    user_id: PositiveInt
    name: Taskname 
    description: Description
    stat: Status  
    created_at: dt.datetime

    model_config = ConfigDict(from_attribute=True)


class TaskResp(Response):
    id: PositiveInt 
    user_id: PositiveInt
    name: Taskname
    description: Description
    stat: Status
    created_at: dt.datetime
     

# Validation functions
def is_valid_task_name(task_name: str | None) -> str | None:
    if not task_name:
        return None

    valid_chars = string.ascii_letters + string.ascii_digits 
    valid = (len(set(task_name)) == len(set(task_name) & set(valid_chars)))

    if not valid:
        raise ValueError(f"{task_name} is not a valid task name!")

    return task_name
