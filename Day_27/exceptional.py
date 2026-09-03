#try - check weather there is error or not
'''
try:
    #a = int(input())
    K = {1:12,12:13}
    #print(K[14])
    l = [232,54]
    #print(l[10])
    #print(10/0)
    #print('l'+1)
except ValueError:
    print("Enter the correct datatype")
except KeyError:
    print("Key is not there")
except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("Can't divide with zero")
except TypeError:
    print("Enter the correct datatype")
except NameError:
    print("Define the variable")
else:
    print("Error free program")
finally:
    print("End of the program")
'''
'''
try:
    #a = int(input())
    K = {1:12,12:13}
    #print(K[14])
    l = [232,54]
    #print(l[10])
    #print(10/0)
    #print('l'+1)
except (ValueError,KeyError,IndexError,ZeroDivisionError,TypeError,NameError) as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")
'''
#Recommended one
'''
try:
    #a = int(input())
    K = {1:12,12:13}
    #print(K[14])
    l = [232,54]
    print(l[10])
    #print(10/0)
    #print('l'+1)
except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")
'''
try:
    amount = int(input("Enter the amount: "))
    balance = 5000
    if amount < 0:
        raise Exception("Amount needs to be positive")
except Exception as e:
    print("Error occured: ",e)
else:
    print("Error free program")
finally:
    print("End of the program")