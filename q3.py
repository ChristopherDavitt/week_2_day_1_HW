age = int(input("What is your age? "))
if age < 18:
    print(f"Your age is {age}, you must be a kid")
elif age >= 18 and age < 65:
    print(f"Your age is {age}, you must be an adult")
else: 
    print(f"Your age is {age}, you must be a senior")