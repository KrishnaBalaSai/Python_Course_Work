from abc import ABC, abstractmethod

class Customer:
    def __init__(self, customer_id, name, email, phonenumber, age, income, credit_score):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phonenumber = phonenumber
        self.age = age
        self.income = income
        self.credit_score = credit_score

    def check_eligibility(self):
            if self.age < 21 or self.credit_score < 650 or self.income < 25000:
                return False
            return True
    
    def display_customer(self):
        print("\nCustomer Details")
        print("----------------")
        print("Customer ID  :", self.customer_id)
        print("Name         :", self.name)
        print("Email        :", self.email)
        print("Phonenumber  :", self.phonenumber)
        print("Age          :", self.age)
        print("Income       :", self.income)
        print("Credit Score :", self.credit_score)

class Loan(ABC):
    def __init__(self,loan_id,customer,loan_amount,interest_rate,tenure):
        self.loan_id = loan_id
        self.customer = customer
        self.__loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.tenure = tenure
        self.__balance = loan_amount
        self.__total_paid = 0
        self.repayment_history = []
        self.status = "Applied"

    @abstractmethod
    def calculate_emi(self):
        pass

    def check_loan_eligibility(self):

        if not self.customer.check_eligibility():
            self.status = "Rejected"
            return False

        return True

    def sanction_loan(self):
        if self.status == "Rejected":
            print("Loan application was rejected")
            return

        if not self.check_loan_eligibility():
            print("Customer is not eligible for the loan")
            return

        self.status = "Sanctioned"

        print("\nLoan sanctioned successfully")

    def repay(self, amount):

        if self.status != "Sanctioned":
            print("Repayment is not allowed")
            print("Loan Status:", self.status)
            return

        if amount <= 0:
            print("Invalid repayment amount")
            return

        if amount > self.__balance:
            print("Repayment amount is greater than outstanding balance")
            return

        self.__balance -= amount
        self.__total_paid += amount

        self.repayment_history.append(amount)

        print("\nRepayment successful")
        print("Amount Paid          :", amount)
        print("Outstanding Balance  :", self.__balance)

        if self.__balance == 0:
            self.status = "Closed"
            print("Loan closed successfully")

    def get_balance(self):
        return self.__balance

    def get_loan_amount(self):
        return self.__loan_amount

    def get_total_paid(self):
        return self.__total_paid

    def display_statement(self):

        print("\n")
        print("=" * 40)
        print("LOAN STATEMENT")
        print("=" * 40)

        print("Loan ID              :", self.loan_id)
        print("Customer Name        :", self.customer.name)
        print("Loan Amount          :", self.__loan_amount)
        print("Interest Rate        :", self.interest_rate)
        print("Tenure               :", self.tenure)
        print("Total Paid           :", self.__total_paid)
        print("Outstanding Balance  :", self.__balance)
        print("Loan Status          :", self.status)

        print("\nRepayment History")

        if not self.repayment_history:
            print("No repayments made")

        else:
            for i in range(len(self.repayment_history)):
                print(f"Payment {i+1}          : {self.repayment_history[i]}")

        print("=" * 40)

    def __str__(self):

        return (
            f"Loan ID: {self.loan_id}, "
            f"Customer: {self.customer.name}, "
            f"Loan Amount: {self.__loan_amount}, "
            f"Outstanding: {self.__balance}, "
            f"Status: {self.status}"
        )


class HomeLoan(Loan):

    def calculate_emi(self):

        principal = self.get_loan_amount()
        monthly_rate = self.interest_rate / (12 * 100)
        months = self.tenure * 12

        emi = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

        return round(emi, 2)


class PersonalLoan(Loan):

    def calculate_emi(self):

        principal = self.get_loan_amount()
        monthly_rate = self.interest_rate / (12 * 100)
        months = self.tenure * 12

        emi = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

        return round(emi, 2)


class CarLoan(Loan):

    def calculate_emi(self):

        principal = self.get_loan_amount()
        monthly_rate = self.interest_rate / (12 * 100)
        months = self.tenure * 12

        emi = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

        return round(emi, 2)

Krishna = Customer(1,'krishna','krishna32@gmail.com',9876543210,21,50000,750)
Krishna.display_customer()
print("Loan Eligibility:",Krishna.check_eligibility())


Sai = Customer(1,'sai','sai234@gmail.com',9876543210,21,60000,600)
Sai.display_customer()
print("Loan Eligibility:",Sai.check_eligibility())

home_loan = HomeLoan(
    "HL1001",
    customer1,
    500000,
    8.5,
    10
)


customer1.display_customer()

print("\nLoan Application")
print("----------------")

print(home_loan)

print("\nChecking Loan Eligibility")

if home_loan.check_loan_eligibility():

    print("Customer is eligible")

    home_loan.sanction_loan()

    print("\nEMI")
    print("Monthly EMI:", home_loan.calculate_emi())

    print("\nRepayments")

    home_loan.repay(100000)
    home_loan.repay(150000)
    home_loan.repay(250000)

else:

    print("Customer is not eligible")


print("\nFinal Loan Details")
print(home_loan)

home_loan.display_statement()