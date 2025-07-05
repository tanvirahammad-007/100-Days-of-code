#Tip Calculator
print("Welcome to Bill Spliter Calculator!")

a = float(input("What was the total Bill? "))
b = int(input("How much money would you like to give? (5,10,15): "))
c = int(input("How many people to split the bill? "))

final = float((a+b)/c)
print("Each person should pay" , final)