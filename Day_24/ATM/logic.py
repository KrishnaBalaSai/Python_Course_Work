data = {
    123456: {'pin':1234,'balance':7000,'history':[]},
    234561: {'pin':1234,'balance':5000,'history':[]},
    345612: {'pin':1234,'balance':6000,'history':[]},
    456123: {'pin':1234,'balance':9000,'history':[]}
}

def menu():
    print('[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transactions')
    print('[E]xit')


def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login Successful")
        return True
    else:
        print("Invalid Login")
        return False

def checkbalance():
    print("Current Balance:",data[acc_num]['balance'])

def deposit():
    amount = int(input("Enter the amount: "))
    data[acc_num]['balance'] += amount
    print(f'{amount} is successfully deposited')
    data[acc_num]['history'].append(f'{amount} is deposited+++++++')

def withdraw():
    amount = int(input("Enter the amount: "))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance'] -= amount
        print(f'{amount} is successfully withdraw')
        data[acc_num]['history'].append(f'{amount} is withdraw-------')
    else:
        print("Insufficent Balance")


def viewtransactions():
    if data[acc_num]['history']:
        print("--------------Transactional History-----------")
        for i in data[acc_num]['history']:
            print(i)
    else:
        print("No Trasaction History")