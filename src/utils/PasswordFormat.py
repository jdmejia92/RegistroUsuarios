from werkzeug.security import generate_password_hash

class PasswordFormat():

    @classmethod
    def convert_password(self,password):
        return generate_password_hash(password, method='pbkdf2')