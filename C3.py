# C3. Decimal to Binary
# division by 2 (no bin())

def decimal_to_binary(n):       # Defining a function to convert a decimal number into its binary strin representation
    if n == 0:                  # 0 is a special case in which  the loop below would skip it and return an empty string

        return "0"
    binary = ""

    
    while n > 0:                    # dividing by 2 until nothing is left
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
        
    return binary                   # Return the final complete binary string


print("decimal_to_binary(10) ->", decimal_to_binary(10))  # Testing the function with the number 10

print("decimal_to_binary(25) ->", decimal_to_binary(25))  # Testing the function with the number 25
