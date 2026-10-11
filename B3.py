# Sensor Readings

#it is a tuple containing a collection of sensor voltage readings
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)   

above_count = 0
highest = readings[0]           # Assuming that the first reading is initially the highest
lowest = readings[0]
total = 0                       # Assuming that the first reading is initially the lowest

for reading in readings:
    if reading > 3.2:                       # Check if the current reading is greater than 3.2 V
        above_count = above_count + 1
        
    if reading > highest:                   # Check if the current reading is higher than our current maximum
        highest = reading
        
    if reading < lowest:                    # Check if the current reading is lower than our current minimum
        lowest = reading
        
    total = total + reading                 # Add the current reading to the running total
    
# Calculate the average by dividing the total sum by the total number of readings
average = total / len(readings)

print("Readings above 3.2 V:", above_count)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", round(average, 2), "V")
