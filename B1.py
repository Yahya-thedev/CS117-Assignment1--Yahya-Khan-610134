#current through a 10 ohm resistor for 1 V to 10 V




resistance = 10     #we have the fixed resistance


#intead of applying voltage manually in formula we are  using for loop

for voltage in range(1, 11):       # i specified the range of which voltage should the loop runs
    
    current = voltage / resistance     #applied the formula
    print("V =", voltage, "V, I =", current, "A")
