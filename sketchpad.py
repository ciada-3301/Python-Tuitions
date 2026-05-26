def traingle_area():
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    return 0.5*base*height

def frustum():
    a1 = int(input("Enter Lower radius (R): ")) 
    a2 = int(input("Enter Upper radius (r): ")) 
    h =  int(input("Enter the height (h): "))   
    volume = 0.33 * 3.14 * h * (a1**2 + a2**2 + a1*a2)
    return volume

frustum1 = frustum()
frustum2 = frustum()
frustum3 = frustum()
frustum4 = frustum()



