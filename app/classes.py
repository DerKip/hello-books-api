
class User():
    """ Contains user data """

    users=[] #list for all users

    def __init__(self):
        self.public_id=None
        self.name=None
        self.password=None
        self.admin=False
    