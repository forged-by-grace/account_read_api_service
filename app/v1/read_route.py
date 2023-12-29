from fastapi import APIRouter, Depends
from core.utils.settings import *
from core.controller.read_controller import *
from core.helper.account_helper import verify_access_token

from typing import Annotated

from core.model.token_model import VerifyTokenResponse
from core.model.account_model import CurrentAccount

account_read_route = APIRouter(
    prefix=f"{settings.api_prefix}accounts",
    tags=['Read Account ']
)


@account_read_route.get('/current-account/', description='Retrieve the current logged in account data', response_model=CurrentAccount)
async def get_current_account(current_account: Annotated[VerifyTokenResponse, Depends(verify_access_token)]):
    return await current_account_ctrl(current_account=current_account)


# @account_read_route.get('/', description='Retrieve accounts', dependencies=[Depends(is_Admin)])
# async def get_accounts(skip: int, limit: int):
#     return await get_accounts_ctrl(skip=skip, limit=limit)


# @account_read_route.get('/id/{account_id}', description='Retrieve a single account using the account id', response_model=AccountInDB, dependencies=[Depends(is_Admin)])
# async def get_account_by_id(account_id: str):
#     return await get_account_by_id_ctrl(id=account_id)


# @account_read_route.get('/email/{email}', description='Retrieve an account using the email address', response_model=AccountInDB, dependencies=[Depends(is_Admin)])
# async def get_account_by_email(email: EmailStr):
#     return await get_account_by_email_ctrl(email=email)


# @account_read_route.get('/username/{username}', description='Retrieve an account using the username', response_model=AccountInDB, dependencies=[Depends(is_Admin)])
# async def get_account_by_username(username: str):
#     return await get_account_by_username_ctrl(username=username)


# @account_read_route.get('/phone_number/{phone_number}', description='Retrieve an account using the phone number', response_model=AccountInDB, dependencies=[Depends(is_Admin)])
# async def get_account_by_phone_number(phone_number: str):
#     return await get_account_by_phone_number_ctrl(phone_number=phone_number)


# @account_read_route.get('/firstname/{firstname}', description='Retrieve an account using the firstname', response_model=AccountInDB, dependencies=[Depends(is_Admin)])
# async def get_accounts_by_firstname(firstname: str, skip: int, limit: int):
#     return await get_accounts_by_firstname_ctrl(firstname=firstname, skip=skip, limit=limit)


# @account_read_route.get('/lastname/{lastname}', description='Retrieve an account using the lastname', response_model=AccountInDB, dependencies=[Depends(is_Admin)])
# async def get_accounts_by_lastname(lastname: str, skip: int, limit: int):
#     return await get_accounts_by_lastname_ctrl(lastname=lastname, skip=skip, limit=limit)


# @account_read_route.get('/created-on/{created_on}', description='Retrieve all accounts created on a specific date', response_model=AccountInDB, dependencies=[Depends(is_Admin)])
# async def get_accounts_by_date_created(created_on: datetime, skip: int, limit: int):
#     return await get_accounts_by_date_created_ctrl(created_on=created_on, skip=skip, limit=limit)


# @account_read_route.get('/created/from/{start_date}/to/{end_date}', description='Retrieve all accounts created within a specified period', dependencies=[Depends(is_Admin)])
# async def get_accounts_created_within_a_period(start_date: datetime, end_date: datetime, skip: int, limit: int):
#     return await get_accounts_created_within_a_period_ctrl(start_date=start_date, end_date=end_date, skip=skip, limit=limit)


# @account_read_route.get('/last-update/{last_update}', dependencies=[Depends(is_Admin)])
# async def get_accounts_by_last_update(last_update: datetime, skip: int, limit: int):
#     return await get_accounts_by_last_update_ctrl(last_update=last_update, skip=skip, limit=limit)


# @account_read_route.get('/last-update/from/{start_date}/to/{end_date}', description="Retrieve an account updated within a specified period.", dependencies=[Depends(is_Admin)])
# async def get_accounts_updated_with_a_period(start_date: datetime, end_date: datetime, skip: int, limit: int):
#     return await get_accounts_updated_within_a_period_ctrl(start_date=start_date, end_date=end_date, skip=skip, limit=limit)


