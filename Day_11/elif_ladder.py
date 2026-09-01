'''Q3. Hostinger Hosting Plan
Write a Python program to determine the hosting plan based on the customer's budget.
Conditions:
● Above ₹10000 → Cloud Hosting
● Above ₹5000 → Business Hosting
● Above ₹2000 → Premium Hosting
● Otherwise → Single Hosting'''

budget = int(input())
if budget > 10000:
    print("Cloud Hosting")
elif budget > 5000:
    print("Business Hosting")
elif budget > 2000:
    print("Premium Hosting")
else:
    print("Single Hosting")