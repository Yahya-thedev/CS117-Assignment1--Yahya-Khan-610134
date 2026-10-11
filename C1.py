# C1. Current and Power 



def ohms_current(v, r):             # Defining a function to calculate current using fformula "I = V / R"
    return v / r


def power_dissipated(i, r):         # Defining a function to calculate power dissipated in a resistor using  "P = I^2 * R"
    return i ** 2 * r


current = ohms_current(12, 6)       # Calculating the current with the help of  12 Volts and 6 Ohms of resistance


power = power_dissipated(current, 6)    # Calculating the power dissipated using the calculated current and the same 6 Ohms resistance



# final results
print("Current =", current, "A")
print("Power =", power, "W")
