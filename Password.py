password = "python123"
max_attempts = 3
used_attempts = 0

while used_attempts < max_attempts:
    entered_password = input("Enter the password: ")
    if entered_password == password:
        print("Welcome.")
        break
    else:
        print("Wrong, try again.")
        used_attempts += 1

        if used_attempts == max_attempts:
            print("No more attempts left...")
            break
