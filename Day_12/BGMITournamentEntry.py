reg=eval(input("Enter regestered or not: "))
fee=eval(input("Enter Fee paid or not: "))
if reg:
    if fee:
        print("Tournament Entry Confirmed")
    else:
        print("pending entry fee")
else:
    print("Registration Required")