from fastapi import Request
from core.helper.request_helper import *

from core.utils.init_log import logger
from core.utils.error import credential_error

from core.model.token_model import VerifyTokenResponse

from core.helper.cache_helper import get_account_from_cache
from core.helper.db_helper import get_account_by_id

from core.utils.settings import settings
from fastapi import HTTPException, status


async def verify_token(url: str, request: Request):
    # Get access token from request
    logger.info('Checking if header has authorization token')
    token_data = request.headers.get('Authorization')
    if not token_data:
        raise credential_error
    
    # Extract data
    token_type = token_data.split()[0]
    token = token_data.split()[1]

    # Check if token type is Bearer
    logger.info('Checking if token type is Bearer.')
    if not token_type or token_type != 'Bearer':
        raise credential_error
    
    # Check if access token was provided
    logger.info('Checking authorization token was found.')
    if not token:
        raise credential_error
    
    # Create request header
    headers = {
        'Authorization': f"Bearer {token}",
        'content-type': 'appication/json'
    }
    
    # Get response
    logger.info('Sending verify access token request to authorization server.')
    status_code, response = await send_get_request(url=url, headers=headers)

    if status_code >= 400:
        logger.warning(f'Failed to verify authorization token due to error: {str(response)}')
    
    logger.info('Token is valid.')
    return status_code, response, token
    

async def verify_access_token(request: Request):
   # Send request
    status_code, response, token = await verify_token(url=settings.api_verify_access_token_url, request=request)

    # Check status code
    if status_code >= 400:
        raise credential_error
    
    # Create obj
    token_data = VerifyTokenResponse(**response)

    return token_data


async def get_account_from_cache_or_db_by_id(id: str):
    account_data = {}

    # Check if account is in Cache
    account_data: dict = await get_account_from_cache(id=id)
    
    if account_data:  
       return account_data
    else:
        account_data = await get_account_by_id(id=id)
        if account_data:
            return account_data
        else:
            return None
