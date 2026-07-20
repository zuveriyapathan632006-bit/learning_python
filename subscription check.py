#subscription usage calculator
app= input("Name of the app you use:")
usage =int( input("How many times in a month do you use the app? "))
subscription =int(input("Enter the subscription amount"))
calculate_usage =( (subscription / 30) * usage) / subscription * 100
print(f"Your usage is {calculate_usage}%")
if calculate_usage >= 60:
    print(("Your subscription for{app} is used effectively. Continue to subscribe"))
else :
    print(("Subscription for {app} not used effectively"))