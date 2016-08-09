from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

class User:
    def __init__(self, id, email, password, su_status, admin_status, theone_status):
        self.id = id
        self.email = email
        self.is_superuser = su_status
        self.is_admin = admin_status
        self.is_theone = theone_status
        self.password_hash = pwd_context.encrypt(password)

    def generate_auth_token(self, expiration = 600, secret=""):
        s = Serializer(secret, expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token, user_factory, secret=""):
        s = Serializer(secret)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = user_factory.get_by_id(data['id'])
        return user
        

    def hash_password(self, password):
        password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def is_superuser(self):
        return self.is_superuser

    def is_admin(self):
        return self.is_admin
    
    def is_theone(self):
        return self.is_theone

    def update(self, data):
        self.email = data['email']
        self.hash_password(data['password'])
        pass