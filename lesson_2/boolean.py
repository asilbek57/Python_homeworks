#Q1
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
if username == "" and password == "":
    print("Both username and password are empty")
else:
    print("Username and password aren't empty")

#Q2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number : "))
if num1 == num2:
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num1} is not equal to {num2}")

#Q3
num3 = int(input("Enter a number: "))
if num3>=0 and num3 %2 == 0:
    print(f"{num3} is positive and even")
else:
    print(f"{num3} is not both positive and even")

