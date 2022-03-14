from flask import request
from config import BEARER_TOKEN

def auth_required():
    def dec(handler):
        def wrapper(*args, **kwargs):
            auth = request.headers.get("Authorization")

            if auth is None or auth[:6] != 'Bearer':
                return dict(error = "Need Bearer auth")

            if auth[7:] == BEARER_TOKEN:
                return handler(*args, **kwargs)
                
            else:
                return dict(error = "Invalid token")

        return wrapper

    return dec


