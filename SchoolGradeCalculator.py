name = input("Enter your name: ")

print("Let's calculate your average and see if you passed.")

grade1 = input("Enter your first grade: ")
grade2 = input("Enter your second grade: ")

try:
    grade1_float = float(grade1)
    grade2_float = float(grade2)
    result = (grade1_float + grade2_float) / 2

except:
    ...

if result >= 6:
    print(f"The student {name} passed with {result} points.")
elif result >= 4.9:
    print(f"The student {name} is in recovery with {result} points.")
elif result < 4:
    print(f"The student {name} failed with {result} points.")
