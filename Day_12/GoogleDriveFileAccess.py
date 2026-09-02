act = eval(input("Link Active: "))
if act:
    per = eval(input("Permission Granted: "))
    if per:
        print("File Opened Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")