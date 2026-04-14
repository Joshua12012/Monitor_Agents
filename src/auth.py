from fastapi import Header, HTTPException, Depends
from dotenv import load_dotenv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import os

load_dotenv()
security = HTTPBearer()

API_TOKEN = os.getenv("API_TOKEN")
                                        #  ... -> means field is required
def verify_token(authorization: str = Header(...)):
    print(">>> Incoming Authorization Header:", authorization)
    print(">>> Expected:", f"Bearer {API_TOKEN}")
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=401, detail="Invalid token")

# def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
#     token = credentials.credentials
    
#     if token != API_TOKEN:
#         raise HTTPException(status_code=401, detail="Invalid token")

