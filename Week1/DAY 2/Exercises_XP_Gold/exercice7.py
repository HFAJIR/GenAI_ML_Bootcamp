
# Create a list of numbers from 1 to 1,000,000
numbers = list(range(1, 1000001))

# Check if list starts at 1 and ends at 1,000,000
if min(numbers) == 1 and max(numbers) == 1000000:
    print("The list starts at 1 and ends at 1,000,000.")
else:
    print("The list does not start at 1 or end at 1,000,000.")  

# Calculate and display the sum
total_sum = sum(numbers)
print("The sum of all numbers from 1 to 1,000,000 is:", total_sum)