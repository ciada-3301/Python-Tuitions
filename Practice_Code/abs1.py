# Problem : take user_input....if user input is > 10 print (user_input*12)
#usr input 0-10, print(user_input)
#less than 0 print(usrinp *-12)

usr_inp = int(input("Enter the number: "))

if usr_inp > 10 :
    print(usr_inp*12)

elif usr_inp in range(0,11) :  # 0 1 2 3 4 5 6 7 8 9 10
    print(usr_inp)

elif usr_inp < 0 :
    print(usr_inp * -12)