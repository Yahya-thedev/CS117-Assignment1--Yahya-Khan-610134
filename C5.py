# C5. Star-Delta (Y-Δ) Transformation


# Defining a function to convert Star (Y) resistors  into Delta resistors 
def star_to_delta(ra, rb, rc):                  # ra, rb, rc are the three resistors of the star network
    
    
    numerator = ra * rb + rb * rc + rc * ra     # Calculating the sum of all pairwise products of the star resistors used as the numerator for all formulas

    rab = numerator / rc
    rbc = numerator / ra
    rca = numerator / rb


    return round(rab, 2), round(rbc, 2), round(rca, 2)              # return the three delta resistances rounded to 2 decimal places



print("star_to_delta(10, 20, 30) ->", star_to_delta(10, 20, 30))    # testing with the sample values
