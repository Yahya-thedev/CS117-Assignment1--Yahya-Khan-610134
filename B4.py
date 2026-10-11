#B4. Continuous Discharge Analysis


# list of voltage readings taken 
voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]


# Trackers to save the overall longest continuous dropping streak found
best_length = 1
best_start = voltages[0]
best_end = voltages[0]

# Trackers for the current dropping streak being evaluated in the loop
current_length = 1
current_start = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:                   # Check if the voltage dropped compared to the previous minute
        current_length = current_length + 1                     # still dropping, extend the streak
    else:
        # streak broken, start a new one from this reading
        current_length = 1
        current_start = voltages[i]

    # only replace if strictly longer, so the first longest streak is kept
    if current_length > best_length:
        best_length = current_length
        best_start = current_start
        best_end = voltages[i]

print("Longest continuous drop:", best_length, "minutes")
print("Started at:", best_start, "V")
print("Ended at:", best_end, "V")





