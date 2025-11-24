# app/Mail/model.py
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from typing import Optional, List

PyObjectId = Annotated[str, BeforeValidator(str)]


class MailModel(BaseModel):
    """
    Container for a single require mail entry.
    """
    # The primary key for the StudentModel, stored as a `str` on the instance.
    # This will be aliased to `_id` when sent to MongoDB,
    # but provided as `id` in the API requests and responses.
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    organization: str = Field(...)
    email: EmailStr = Field(...)
    phoneNumber: str = Field(...)
    description: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Project Alpha",
                "email": "jdoe@example.com",
                "organization": "Example Corp",
                "phoneNumber": "+1234567890",
                "description": "A sample project description.",  
                  
            }
        },
    )