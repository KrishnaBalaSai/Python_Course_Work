class Hotstar:
    def __init__(self,name):
        print(f"Welcome to the Hotstar, {name}")
    def login(self):
        print("You can login to the hotstar")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def playcontrollers(self):
        print("pause.resume.play")
    def history(self):
        print("You can see the recent video")
    def ads(self):
        print("Ads will run")
    def quality(self):
        print("Quality is low")
    def access(self):
        print("You have limited access")
    def download(self):
        print("You cannot download high qaulity videos")

class PremiumHotstar(Hotstar):

    def __init__(self, name):
        self.name = name
        print(f"Dear {self.name}, Welcome to the Hotstar!!")

    def ads(self):
        print("Ads will not run")

    def quality(self):
        print("Quality is High")

    def access(self):
        print("You have unlimited access")

    def download(self):
        print("You can download high qaulity videos")



a = Hotstar("Krishna")
a.login()
a.dashboard()
a.search()
a.playcontrollers()
a.history()
a.ads()
a.quality()
a.access()
a.download()


b = PremiumHotstar("Sai")
b.login()
b.dashboard()
b.search()
b.playcontrollers()
b.history()
b.ads()
b.quality()
b.access()
b.download()