'''Q1. Instagram Story Visibility
Write a Python program to check whether a user can view a Close Friends story.
Conditions:
● Check whether the user follows the account.
● If the user follows the account, check whether they are in the Close Friends list.
● If both conditions are True, display "Story Visible".
● Otherwise display the appropriate message.
Test Case 1
Input:
Follows Account: True
Close Friend: True
Output:
Story Visible
Test Case 2
Input:
Follows Account: True
Close Friend: False
Output:
Not in Close Friends List
Test Case 3
Input:
Follows Account: False
Close Friend: False
Output:
Follow the Account First'''
fa=eval(input("Follows Account: "))
cf=eval(input("Close Friends: "))
if fa:
    if cf:
        print("Story Visible")
    else:
        print("Not in Close Friends List")
else:
    print("Follow the Account First")