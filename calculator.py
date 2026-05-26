# Calculator.py
import math

print("Calculator Program")
print("Enter 1 for Addition")
print("Enter 2 for Substraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 for Exponent")

choice = int(input("Enter your choice: "))

if choice==1:
    expression = input("Enter the addition expression: ")
    print("The answer is: ", eval(expression))

if choice==2:
    expression = input("Enter the substraction expression: ")
    print("The answer is: ", eval(expression)) 

if choice==3:
    expression = input("Enter the multiplication expression: ")
    print("The answer is: ", eval(expression))  

if choice ==4:
    numerator = int(input("ENter the numerator: "))  
    denominator = int(input("Enter the denominator: "))  

    nume_factor = []
    denom_factor = []
    

    for factor in range(1,numerator + 1):
        if numerator%factor==0:
            nume_factor.append(factor)

    for factor in range(1,denominator + 1):
        if denominator%factor==0:
            denom_factor.append(factor)

    factor_list = list(set(nume_factor).intersection(denom_factor))
    hcf = max(factor_list)
    new_numerator = numerator / hcf
    new_denominator = denominator / hcf
    if new_denominator == 1.0 :
        print("The simplified fraction is: ", int(new_numerator))
    else:
        print("The simplified fraction is: ", int(new_numerator), "/", int(new_denominator))

if choice==5:
    base = int(input("ENter the base: "))
    power = int(input("ENter the power: "))
    print("The answer is: ", base**power)


    


    

    

