from jwt import encode, decode
from jwt import exceptions
from os import getenv
from flask import jsonify
from datetime import datetime, timezone, timedelta


def write_toke(data:dict):
    token = encode(payload={**data, 'exp':datetime.now(tz=timezone.utc) + timedelta(minutes=5)}, key=getenv('SECREY_KEY'), algorithm='HS256')

    return token.encode('utf-8')

def validate_toke(token, output=False):
    try:
        if output:
            return decode(token, key=getenv('SECREY_KEY'), algorithms=['HS'])
        
        decode(token,key=getenv('SECREY_KEY'), algorithms=['HS256'])
    except exceptions.DecodeError as e:
        response = jsonify({"message":"Invalid Token"})
        response.status_code = 401

        return response
    except exceptions.ExpiresSignatureError as e:
        response = jsonify({"message":"Token Expired"})
        response.status_code = 401

        return response