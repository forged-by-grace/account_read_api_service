from pydantic import EmailStr
from datetime import datetime
from core.helper.cache_helper import *
from core.helper.db_helper import *
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from core.helper.account_helper import get_account_from_cache_or_db_by_id
from core.utils.init_log import logger


async def current_account_ctrl(current_account):
    # Fetch account cache or db
    account_data = await get_account_from_cache_or_db_by_id(id=current_account.id)
    
    if account_data.get('disabled'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Account disabled.'
        )
    
    if not account_data.get('is_active'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Login for access token'
        )
    
    
    return account_data
