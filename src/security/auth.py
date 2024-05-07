import os
from fastapi import Security, HTTPException, status, Depends
from fastapi.security import APIKeyHeader

API_KEY = os.getenv('API_KEY')

api_key_header = APIKeyHeader(name="X-API-Key")

def checkAPIKey(api_key_header: str = Security(api_key_header)) :
    if api_key_header != API_KEY :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid API key"
        )
