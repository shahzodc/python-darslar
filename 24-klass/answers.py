# AMALIYOT

class User:
    def __init__(self,ism,username,email):
        self.ism = ism
        self.username = username
        self.email = email
    
    def get_info(self):
        return f"Foydalanuvchi: {self.ism}\
            username: {self.username}\
                email: {self.email}"
                
    def get_email(self):
        return self.email
    
    def describe():
        pass
    
user  = User("Shahzod","shahzod098",'uzb@gmail.com')
print(user.get_info())
user1 = User("Olim",'uzbek001','olim097@gmail.com')
print(user1.get_email())






 


    