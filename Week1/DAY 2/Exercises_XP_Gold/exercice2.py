
#Range of numbers
print("Multiples of 5 and 7 between 1500 and 2500:")

# Create an empty list to store the results
multiples = []
for number in range(1500,2501):
    if number % 5 == 0 and number % 7 == 0:
        multiples.append(number)

print(multiples)
