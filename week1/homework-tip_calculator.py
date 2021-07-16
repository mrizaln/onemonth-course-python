# get inputs

bill = int(input("How much is the bill? ").replace("$", ''))
tip_percentage = int(input("How much tip do you want (5%, 10%, 15%, 20%)? ").replace("%", '')) / 100

# math
tax_percentage = 0.02

tip = bill * tip_percentage
tax = bill * tax_percentage

total_bill = bill + tip + tax

# printing
print(f"\nyour bill is ${bill}, and your tip is ${tip}")
print(f"your total bill will be ${total_bill}, included with tax and tip")
