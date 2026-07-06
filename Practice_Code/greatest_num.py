num_list = [1,4,3,2,5,6,4,7,8,9,6,1] #list of given numbers

greatest = 0 # dummy initialization of the greatest variable

for num in num_list:  # pull the elements of the list sequentially
    if num>greatest:
        greatest = num # if previous greatest value is smaller than the current value, then the current value is the running greatest.

print(greatest)

