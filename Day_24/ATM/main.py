import logic as lg

if lg.login():
    print("Welcome to the ATM")
    while True:
        lg.menu()
        ch = input("Enter the choice: ").upper()
        if ch=='C':
            lg.checkbalance()
        elif ch == 'D':
            lg.deposit()
        elif ch == 'W':
            lg.withdraw()
        elif ch == 'V':
            lg.viewtransactions()
        elif ch == 'E':
            print("--------Thankyou, Visit Again-------")
            break
        else:
            print("Enter the valid choice")