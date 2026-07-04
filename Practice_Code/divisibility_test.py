# check the divisibility of the given number by a certain number

test_num = int(input("Enter the test number: "))
dividing_num = int(input("Enter the dividing number: "))

# dividing_num divided by test_num
if test_num % dividing_num == 0:
    print("Successfully divided, divisbility test is True")
else:
    print("Divisibility test is false")