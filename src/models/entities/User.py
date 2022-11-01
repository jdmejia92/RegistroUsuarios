class User():
    def __init__(self, id, email=None, password=None):
        self.id = id
        self.email = email
        self.password = password

    def to_JSON(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }
