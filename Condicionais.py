
#simple and powerful!
number1 = input("Choose an number: ")
number2 = input("Choose an number: ")
if number1 > number2:
    print(f"the {number1}is bigger than {number2}")
elif number1 == number2:
    print(f"the {number1} is equal {number2}")
else:
    print(f"the {number2} is bigger than {number1}")

#others with and AND or

question = input("Password: ")
join_or_leave = input("User, you want JOIN or LEAVE: ")
password = "12345"
if question == password and join_or_leave == "JOIN":
    print("joining...")
elif question != password or join_or_leave == "LEAVE":
    print("leaving...")
else:
    print("Reset the program")

# not
not 0 # True
not 1 # False