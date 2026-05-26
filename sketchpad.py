a= int(input("enter the marks for maths"))
b= int(input("enter the marks for science"))
c= int(input("enter the marks for bengali"))
d= int(input("enter the marks for english"))
e= int(input("enter the marks for IT"))
f= int(input("enter the marks for SSC"))
mark_list = [a,b,c,d,e,f]
worst = min(mark_list)
mark_list.remove(worst)
print("Removed: ", worst)

if sum(mark_list)/5>90:
    print("grade a")

elif sum(mark_list)/5>80 and sum(mark_list)/5<=90:
    print("garde b")

elif sum(mark_list)/5>70 and sum(mark_list)/5<=80:
    print("garde c")

elif sum(mark_list)/5>60 and sum(mark_list)/5<=70:
    print("garde d")

else:
    print("Fail bara tui")





