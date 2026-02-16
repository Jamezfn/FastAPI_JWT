from bcrypt import checkpw, hashpw, gensalt

class HashHelper(object):
    @staticmethod
    def verify_password(plain_password: str, hash_password: str):
        if checkpw(plain_password.encode("utf-8"), hash_password.encode("utf-8")):
            return True
        else: 
            return False
        
    @staticmethod
    def get_hashed_password(plain_password: str):
        return hashpw(plain_password.encode('utf-8'), gensalt()).decode('utf-8')