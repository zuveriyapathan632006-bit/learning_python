#Using the birth year and calculating age using it afterwhich using weight in pounds and converting it to KG.
birthyear = input("Enter your birthyear? ")
age = 2026 - int(birthyear)
weight = input("Enter the weight in pounds ")
kg = int(weight) * 0.45
print(f"you are {age} years old and weigh {kg} kg.")