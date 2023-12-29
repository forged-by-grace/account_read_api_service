from core.connection.db_connection import account_col

async def build_single_match_pipeline(filter: dict = {}, page: int = 1, limit: int = 1) -> list[dict]:
    # Calculate skip
    skip = (page - 1) * limit

    # Stage 1: Select account with lastname
    select_account = {'$match': filter}

    # Stage 2: Sort by date of creation
    organize_by_date_created = {'$sort': {'created_at': -1}}

    # Stage 3:
    # Pipeline 1:
    # Count the number of accounts
    account_count = {'$count': 'total_count'}

    # Add current_page field
    add_current_page = {'$addFields': {'current_page': page}}

    # Add page size field
    add_page_size = {'$addFields': {'page_size': limit}}

    # Add total pages field
    add_total_pages = {'$addFields': {'total_pages': {'$divide': ['$total_count', '$page_size']}}}

    # Pipeline 2:
    skip_accounts = {'$skip': skip}

    # Pipeline 3:
    limit_accounts = {'$limit': limit}

    # Pipeline 4:
    account_meta = {'metadata': [account_count, add_current_page, add_total_pages, add_page_size]}

    # Pipeline 5:
    account_data = {'data': [skip_accounts, limit_accounts]}

    # Pipeline 6:
    account_projection = {'$project': {'hashed_password': 0}}

    # Pipeline 7:
    retrieve_accounts = {'$facet': {account_meta, account_data, account_projection}}
    
    # Build pipeline
    pipeline = [select_account, organize_by_date_created, retrieve_accounts]

    results = await account_col.aggregate(pipeline=pipeline)
