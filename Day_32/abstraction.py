from abc import ABC, abstractmethod
class phonepay(ABC):
    def senderinfo(self):
        print("you can enter their mobile number or scanner")
    def amount(self):
        print("you can enter amount")
    def pin(self):
        print("you need to enter the pin")

    @abstractmethod
    def transaction(self):
        pass
class HDFC(phonepay):
    def transaction(self):
        print("payment using hdfc bank")
class SBI(phonepay):
    def transaction(self):
        print("payment using sbi bank")
class UNION(phonepay):
    def transaction(self):
        print("payment using union bank")
class AXIS(phonepay):
    def transaction(self):
        print("payment using axis bank")
class ICIC(phonepay):
    def transaction(self):
        print("payment using icic bank")

Krishna=HDFC()
Krishna.senderinfo()
Krishna.amount()
Krishna.pin()
Krishna.transaction()

Bala=SBI()
Bala.senderinfo()
Bala.amount()
Bala.pin()
Bala.transaction()

Sai=AXIS()
Sai.senderinfo()
Sai.amount()
Sai.pin()
Sai.transaction()