
try:
    your_age = int(input("What is your age? "))
    friend_age = int(input("What is your friends age? "))
    difference = abs(your_age - friend_age)
    print(f"The difference between you two is {difference}")
    
except:
        print("!!! THAT IS NOT A NUMBER, please try using integers !!!")
        