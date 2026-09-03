# Single Inheritance
'''
class whatsappV1:
    def messaging(self):
        print("You can message")

class whatsappV2(whatsappV1):
    def calls(self):
        print("You can audio and video calls")
a = whatsappV1()
a.messaging()

b = whatsappV2()
b.messaging()
b.calls()
'''
# Multilevel Inheritance
'''
class whatsappV1:
    def messaging(self):
        print("You can message")

class whatsappV2(whatsappV1):
    def calls(self):
        print("You can audio and video calls")

class whatsappV3(whatsappV2):
    def status(self):
        print("You can add the status for 24 hours")

a = whatsappV1()
a.messaging()

b = whatsappV2()
b.messaging()
b.calls()

c = whatsappV3()
c.messaging
c.calls()
c.status()
'''
# Multiple Inheritance

'''
class whatsappV1:
    def messaging(self):
        print("You can message")

class whatsappV2:
    def calls(self):
        print("You can audio and video calls")

class whatsappV3(whatsappV1,whatsappV2):
    def status(self):
        print("You can add the status for 24 hours")

a = whatsappV1()
a.messaging()

b = whatsappV2()
b.calls()

c = whatsappV3()
c.messaging
c.calls()
c.status()

'''
# Hierarchical Inheritance
'''
class whatsappV1:
    def messaging(self):
        print("You can message")

class whatsappV2(whatsappV1):
    def calls(self):
        print("You can audio and video calls")

class whatsappV3(whatsappV1):
    def status(self):
        print("You can add the status for 24 hours")

a = whatsappV1()
a.messaging()

b = whatsappV2()
b.messaging()
b.calls()

c = whatsappV3()
c.messaging
c.status()
'''
# Hybrid Inheritance
'''
class whatsappV1:
    def messaging(self):
        print("You can message")

class whatsappV2:
    def extrememessage(self):
        print("You can add emojis, stickers and gifs")

class whatsappV3(whatsappV1,whatsappV2):
    def calls(self):
        print("You can audio and video calls")

class whatsappV4(whatsappV3):
    def status(self):
        print("You can add the status for 24 hours")

a = whatsappV1()
a.messaging()

b=whatsappV2()
b.extrememessage()

c = whatsappV3()
c.messaging()
c.extrememessage()
c.calls()

d = whatsappV4()
d.messaging
d.extrememessage()
d.calls()
d.status()

'''
# Using super() -> Same method + want parent method also → use super()
'''
class whatsappV1:
    def status(self):
        print("You can add images and videos")

class whatsappV2(whatsappV1):
    def status(self):
        super().status()
        print("You can add music and stickers")

class whatsappV3(whatsappV2):
    def status(self):
        super().status()
        print("You can like and you can add reaction")

a = whatsappV3()
a.status()
'''
class whatsappV1:
    def status(self):
        print("You can add images and videos")

class whatsappV2:
    def status(self):
        print("You can add music and stickers")

class whatsappV3(whatsappV1,whatsappV2):
    def status(self):
        whatsappV1.status(self)
        whatsappV2.status(self)
        print("You can like and you can add reaction")

a = whatsappV3()
a.status()