from dataclasses_avroschema.pydantic import AvroBaseModel
from pydantic import Field, EmailStr
from typing import Optional


class CurrentAccount(AvroBaseModel):
    _id: str = Field(description="A unique string representing the account id",
                    json_schema_extra={'id': '7845941214687'}, alias='_id')
    email: EmailStr = Field(description="An email string. This is the user's email address. It will be validated before use.", 
                            json_schema_extra={'email':'joe@example.com'},
                            examples=['johndoe@example.com'])
    firstname: str = Field(description="A string. This is the user's first name.",
                           examples=['John'])
    lastname: str = Field(description="A string. This is the user's lastname.",
                          examples=['Doe'])
    phone_number: str = Field(description="A string. This is the user's mobile or contact number. This will be validated before use.",
                              examples=['915 1234 789'])
    country_code: str = Field(description="A string. This is the user's country code.",
                              examples=['+234'])
    country: str = Field(description="A string. This is the user's country of residence. e.g. Nigeria", 
                         examples=['Nigeria'])
    display_pics: Optional[str] = Field(description='Account display image',)
    email_verified: bool = Field(description="A boolean used to check the verification state of the account's email")
    phone_verified: bool = Field(description="A boolean used to check the verification state of the user's phone number")
    is_active: bool = Field(description="A boolean used to verify the login state of the account")


