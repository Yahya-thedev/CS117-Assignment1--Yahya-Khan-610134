# C4. Loaded Voltage Divider




# Defining a function to calculate output voltage both with and without a load resistor (RL) attached
def loaded_divider(vs, r1, r2, rl):         # vs = supply voltage, r1 = top resistor, r2 = bottom resistor, rl = load resistor

    # Calculating the ideal "unloaded" output voltage using the standard voltage divider formula
    unloaded = vs * r2 / (r1 + r2)

    # r2 and the load are in parallel, so find their equivalent first
    r_parallel = (r2 * rl) / (r2 + rl)

    
    loaded = vs * r_parallel / (r1 + r_parallel)        # Calculating the loaded output voltage by substituting the equivalent parallel resistance into the divider formula

    return round(unloaded, 2), round(loaded, 2)


print("loaded_divider(12, 1000, 1000, 500) ->", loaded_divider(12, 1000, 1000, 500))            # testing with the sample values
