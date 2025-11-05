
#🌟 Exercise 1: Converting Lists into Dictionaries


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Convert lists into a dictionary
my_dict = dict(zip(keys, values))
print(my_dict)

# Alternative method using dictionary comprehension
result = {keys[i]: values[i] for i in range(len(keys))}
print(result)