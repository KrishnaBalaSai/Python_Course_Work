# int float str list tuple set dict bool
#int float str tuple bool - It effects outside values and inside values
#list set dict - there as a passby reference (pass by reference means) It will effect out side also
def display(n):
    n[5] = 6
    print("Inside:",n)
n ={1:2,3:4}
display(n)
print('outside:',n)