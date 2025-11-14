#Cocoa Farm Yield Estimator
bags = int(input("How many bags were harvested:"))
total = bags * 850
print(total)
if bags > 100:
    print(total + 2000)
