# aiologto
 Unofficial Asyncronous Python Client for Logto

 **Latest Version**: [![PyPI version](https://badge.fury.io/py/aiologto.svg)](https://badge.fury.io/py/aiologto)



## Features

- Unified Asyncronous and Syncronous Python Client for [Logto](https://logto.io/)
- Supports Python 3.6+
- Strongly Typed with [Pydantic](https://pydantic-docs.helpmanual.io/)
- Includes Function Wrappers to quickly add to existing projects
- Utilizes Environment Variables for Configuration

---

## Installation

```bash
# Install from PyPI
pip install aiologto

# Install from source
pip install git+https://github.com/GrowthEngineAI/aiologto.git
```

## Usage

WIP - Simple Usage Example

```python
import asyncio
from aiologto import Logto, UserListResponse
from aiologto.utils import logger

"""
Environment Vars that map to Logto.configure:
all vars are prefixed with LOGTO_


LOGTO_URL (url): str takes precedence over LOGTO_SCHEME | LOGTO_HOST | LOGTO_PORT
LOGTO_SCHEME (scheme): str - defaults to 'http://'
LOGTO_HOST (host): str - defaults to None
LOGTO_PORT (port): int - defaults to 3000

LOGTO_APP_ID (app_id): str
LOGTO_APP_SECRET (app_secret): str
LOGTO_RESOURCE (resource): str - defaults to "https://api.logto.io"
LOGTO_OIDC_GRANT_TYPE (oidc_grant_Type): str - defaults to "client_credentials"

## these variables are dynamically generated from the oidc
LOGTO_ACCESS_TOKEN (access_token): str - defaults to None
LOGTO_TOKEN_TYPE (token_type): str - defaults to None

LOGTO_JWT_ALGORITHMS (jwt_algorithms): str - defaults to None
LOGTO_JWT_OPTIONS (jwt_options): dict - defaults to {"verify_at_hash": False}
LOGTO_JWT_ISSUER (jwt_issuer): str - defaults to generated value

LOGTO_TIMEOUT (timeout): int - defaults to 10
LOGTO_IGNORE_ERRORS (ignore_errors): bool = defaults to False

"""

Logto.configure(
    url = '...',
    app_id = "...",
    app_secret = "...",
    debug_enabled = True,
)

async def fetch_users():
    
    # Fetch all the users
    users: UserListResponse = await Logto.users.async_list()
    logger.info(f"Users: {users}")

    # Update a specific user
    user = users[0]
    user.custom_data["email"] = "gexai@example.com"

    user = await Logto.users.async_update(user)
    logger.info(f"User Updated: {user.dict()}")


asyncio.run(fetch_users())

```