#checking wealther the fuse will blow or not
 

voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (ohm): "))

if resistance <= 0:
    print("Invalid resistance")
else:
    #in the next step i applied the I=V/R formula
    current = voltage / resistance
    print("Current =", current, "A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
