start_number = 5
countdown_values = []

# Use a counter so we don't confuse it with the list
current = start_number

# Count down from current down to 1
while current >= 1:
    countdown_values.append(current)
    current -= 1

# After the loop completes, print results
print("Discount countdown complete!")
print(countdown_values)