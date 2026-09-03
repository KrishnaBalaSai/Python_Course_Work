# Using object -> ins,cls,sta,clsatt,insatt
# Using class -> cls,sta,clsatt

'''
class flipkart:
    products = {'shirts':1000,'handbag':2000,'pants':3000}
    discount = 30

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello {self.name},Welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{flipkart.discount}% discount is going on, grab the products......")

krishna = flipkart()
krishna.userinfo('krishna',9398899357,'Hyd')
krishna.displaydiscount()
krishna.display()

print(krishna.products)
print(krishna.name)

flipkart.displaydiscount()
flipkart.display()
print(flipkart.products)
'''
'''
class flipkart:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        print(f"Hello {self.name},Welcome to the flipkart")

krishna = flipkart('krishna',9398899357)
bala = flipkart('bala',9398899356)
sai = flipkart('sai',9398899355)
'''
'''
class instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self,newpost):
        self._posts.append(newpost)

    def display(self):
        print(self.username,self.__password,self._posts)

krishna = instagram('krishna','krishna12#')
krishna.display()
print(krishna.username)
print(krishna.getpassword())
print(krishna.accesspost)

krishna.username = 'sai'
krishna.setpassword('sai123@*#')
krishna.accesspost = "sunrise.png"
krishna.accesspost = "moon.png"
krishna.accesspost = "beach.png"

print(krishna.username)
print(krishna.getpassword)
print(krishna.accesspost)

'''
