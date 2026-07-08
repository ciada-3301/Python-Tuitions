pali = input("Enter the string: ")

length = len(pali)

if length%2==0:
    print("Even charecters")
    split_index = int(length/2)

    up_split = pali[:split_index]
    down_split = pali[split_index:]
    print(up_split, down_split)

    if up_split == down_split[::-1]:
        print("Is palindrome")
    else:
        print("Is not palindrome")

elif length%2 != 0:
    print("Odd charecters")
    split_index =  int((length+1)/2)
    up_split = pali[:split_index-1]
    down_split = pali[split_index:]
    print(up_split, down_split)
    if up_split == down_split[::-1]:
        print("Is palindrome")
    else:
        print("Is not palindrome")



