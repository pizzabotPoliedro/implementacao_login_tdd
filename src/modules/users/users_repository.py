class UsersRepository:
    def __init__(self):
        self.users = {}
    
    def create(self, user):
        email = user["email"]
        if email in self.users:
            raise Exception("Email já existe")
        
        self.users[email] = user
        return True
    
    def get_by_email(self, email):
        if email not in self.users:
            return None
        return self.users[email]
    
    def get_user_to_login(self, email):
        return self.get_by_email(email)
