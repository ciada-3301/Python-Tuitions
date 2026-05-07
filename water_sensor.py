sensor_value = float(input("Enter the Sensor value: "))

tap_state = False

if sensor_value > 100 :
    tap_state = False
    print("Tap is turned off")

elif sensor_value < 10 : 
    tap_state = True
    print("Turning on the tap")

else:
    print(tap_state)

