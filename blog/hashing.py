from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
class hash():
    def bcrypt(password: str):
        return  pwd_cxt.hash(password)