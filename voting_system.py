#EC Voting Eligibility System
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
nationality = input("What is your nationality?: ").lower()
if age >= 18:
    and nationality == "Ghana"
    print(f"{name},you are eligible to vote")
else:
    print(f"{name},you are not eligible to vote")
