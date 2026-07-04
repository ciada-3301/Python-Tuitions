# Calculator.py
import math

print("===== Calculator Program =====")

while True:

    print("\nChoose an option")
    print("1  - Addition")
    print("2  - Subtraction")
    print("3  - Multiplication")
    print("4  - Simplify Fraction")
    print("5  - Exponent")
    print("6  - Trigonometry")
    print("7  - Degree/Radian Conversion")
    print("8  - Multiplication Table")
    print("9  - Square Root")
    print("10 - Logarithm")
    print("0  - Exit")

    choice = int(input("Enter your choice: "))

    # Addition
    if choice == 1:
        expression = input("Enter addition expression: ")
        print("Answer:", eval(expression))

    # Subtraction
    elif choice == 2:
        expression = input("Enter subtraction expression: ")
        print("Answer:", eval(expression))

    # Multiplication
    elif choice == 3:
        expression = input("Enter multiplication expression: ")
        print("Answer:", eval(expression))

    # Simplify Fraction
    elif choice == 4:

        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))

        hcf = math.gcd(numerator, denominator)

        new_numerator = numerator // hcf
        new_denominator = denominator // hcf

        if new_denominator == 1:
            print("Simplified fraction:", new_numerator)
        else:
            print("Simplified fraction:",
                  new_numerator, "/", new_denominator)

    # Exponent
    elif choice == 5:

        base = float(input("Enter base: "))
        power = float(input("Enter power: "))

        print("Answer:", base ** power)

    # Trigonometry
    elif choice == 6:

        print("\nTrigonometry Functions")
        print("1 - Sin")
        print("2 - Cos")
        print("3 - Tan")
        print("4 - Sec")
        print("5 - Cosec")
        print("6 - Cot")


        trig_choice = int(input("Choose function: "))

        angle = float(input("Enter angle in degrees: "))

        radian = math.radians(angle)

        if trig_choice == 1:
            print("sin(", angle, ") =", math.sin(radian))

        elif trig_choice == 2:
            print("cos(", angle, ") =", math.cos(radian))

        elif trig_choice == 3:
            print("tan(", angle, ") =", math.tan(radian))

        elif trig_choice == 4:
            #sec
            print("Sec(", angle, ") =", 1/math.cos(radian))

        elif trig_choice == 5:
            #cosec
            print("Cosec(", angle, ") =", 1/math.sin(radian))

        elif trig_choice == 6:
            #cot
            print("cot(", angle, ") =", 1/math.tan(radian))

        else:
            print("Invalid choice")

    # Degree/Radian Conversion
    elif choice == 7:

        print("\n1 - Degree to Radian")
        print("2 - Radian to Degree")

        convert_choice = int(input("Choose conversion: "))

        if convert_choice == 1:

            degree = float(input("Enter degree: "))
            print("Radian:", math.radians(degree))

        elif convert_choice == 2:

            radian = float(input("Enter radian: "))
            print("Degree:", math.degrees(radian))

        else:
            print("Invalid choice")

    # Multiplication Table
    elif choice == 8:

        number = int(input("Enter number for table: "))
        limit = int(input("Enter limit: "))

        print("\nMultiplication Table of", number)

        for i in range(1, limit + 1):
            print(number, "x", i, "=", number * i)

    # Square Root
    elif choice == 9:

        number = float(input("Enter number: "))
        print("Square Root =", math.sqrt(number))

    # Logarithm
    elif choice == 10:

        number = float(input("Enter number: "))
        print("Natural Log =", math.log(number))

    # Exit
    else:   
        print("Invalid choice")