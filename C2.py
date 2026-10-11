# C2. Parallel Resistance 

# Formula: 1 / R_eq = 1/R1 + 1/R2 + ..........



def parallel_resistance(resistors):   #Defining a function to calculate the total equivalent resistance for resistors connected in parallel
    reciprocal_sum = 0                # Initialization for the sum of reciprocals (1/R)
    
    for r in resistors:
        reciprocal_sum = reciprocal_sum + 1 / r          # Add the reciprocal of the current resistor
    return round(1 / reciprocal_sum, 2)


print("parallel_resistance([10, 10]) ->", parallel_resistance([10, 10]))    # Testing the function with a pair of 10-ohm resistors

print("parallel_resistance([100, 200, 300]) ->", parallel_resistance([100, 200, 300]))      # Testing the function with three different resistors
