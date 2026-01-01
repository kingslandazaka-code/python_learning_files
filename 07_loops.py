
# 7. Loops

# FOR LOOP
# range(5) generates numbers from 0 up to (but not including) 5 → 0,1,2,3,4
for i in range(5):

    # Check if the current value of i is 3
    if i == 3:
        # continue skips the rest of the loop body
        # and jumps straight to the next iteration
        # So when i == 3, print(i) is NOT executed
        continue

    # This runs for all values except 3
    print(i)

# Output:
# 0
# 1
# 2
# 4


# WHILE LOOP
# Initialize a counter variable
count = 0

# The loop keeps running as long as this condition is True
while count < 3:

    # Print the current value of count
    print(count)

    # Increase count by 1
    # Without this line, the loop would run forever (infinite loop)
    count += 1

# Output:
# 0
# 1
# 2

