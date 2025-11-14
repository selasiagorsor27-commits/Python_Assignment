route = input("Enter your route: ")
passengers = int(input("How many passengers: "))

if route == "Accra-Madina":
    fare = 5
elif route == "Accra-Kasoa":
    fare = 10
elif route == "Accra-Tema":
    fare = 8
else:
    fare = 0
    print("Invalid route")

total = fare * passengers

print("Total fare is:", total)

