from jose import jwt
from datetime import datetime, timedelta

SECRET = "secret"

def create_token(data):
    return jwt.encode(
        {**data, "exp": datetime.utcnow() + timedelta(hours=2)},
        SECRET,
        algorithm="HS256"
    )
