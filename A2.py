#finding direction of current flow:


#we are useing float beacuse input of current can be in decimals
current = float(input("Enter current (A): "))

if current > 0:
    print("Current flows from A to B")
elif current < 0:
    print("Current flows from B to A")
else:
    print("No current flows")
