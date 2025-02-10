from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self,id,username,email,password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def check_password(cls,hashed_password,password):
        return check_password_hash(hashed_password,password)
    
    @classmethod
    def generar_password(cls,password):
        return generate_password_hash(password)
    