# Logic Gates

a = int(input("Enter A: "))
b = int(input("Enter B: "))

#we using or becuse in OR condion if one codition is true it runs so here i think OR condition fits best
if (a != 0 and a != 1) or (b != 0 and b != 1):
    print("Bits must be 0 or 1")

else:
    #AND gate outputs 1 only if all of its inputs are 1. If any input is 0, the output is 0
    if a == 1 and b == 1:
        and_out = 1
    else:
        and_out = 0

#OR gate outputs 1 if at least one of its inputs is 1. It only outputs 0 if all inputs are 0
    if a == 1 or b == 1:
        or_out = 1
    else:
        or_out = 0

#XOR gate outputs 1 only if the inputs are different (one is 0 and the other is 1). If both inputs are the same (0 and 0, or 1 and 1), the output is 0
    if a != b:
        xor_out = 1
    else:
        xor_out = 0

    print("AND =", and_out)
    print("OR =", or_out)
    print("XOR =", xor_out)
