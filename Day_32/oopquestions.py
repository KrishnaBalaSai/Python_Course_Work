'''class User:
    def __init__(self,name,email,phone,password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
    def register(self):
        if not self.name:
            print("Registration Failed: Name is required")
        elif not self.email:
            print("Registration Failed: Email is required")
        elif not self.phone:
            print("Registration Failed: phone number is required")
        elif not self.password:
            print("Registration Failed: password is required")
        else:
            print("Registration Successful")
user1 = User(
    "Rahul",
    "rahul@gmail.com",
    "9876543210",
    "rahul123")
user1.register()

user2 = User(
    "Rahul",
    "",
    "9876543210",
    "rahul123"
)
user2.register()
'''
