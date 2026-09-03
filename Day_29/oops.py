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

bala = flipkart()
bala.userinfo('bala',9398899356,'Bang')
bala.displaydiscount()
bala.display()

sai = flipkart()
sai.userinfo('sai',9398899355,'Mrk')
sai.displaydiscount()
sai.display()