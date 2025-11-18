import math

# exercice 1 : Insert item at defined index

print("----- Exercise 1: Insert item at defined index -----")
def insert_item(lst, index, item):
    lst.insert(index, item)
    return lst

# Example
print(insert_item([1, 2, 3], 1, 'a')) 

# Exercise 2: Count spaces in a string

print("----- Exercise 2: Count spaces in a string -----")
def count_spaces(s):
    return s.count(' ')

print(count_spaces("Hello world! How are you?"))  

#Exercise 4: Sum of an array without sum()

print("----- Exercise 4: Sum of an array without sum() -----")

def my_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(my_sum([1,5,4,2])) 

#Exercise 5: Find max in a list

print("----- Exercise 5: Find max in a list -----")

def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([0,1,3,50]))  # 50

# Exercise 6: Factorial of a number

print("----- Exercise 6: Factorial of a number -----")

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4))  # 24

# Exercise 7: Count an element in a list

print("----- Exercise 7: Count an element in a list -----")

def list_count(lst, elem):
    count = 0
    for i in lst:
        if i == elem:
            count += 1
    return count

print(list_count(['a','a','t','o'],'a'))  # 2

# Exercise 8: L2-norm of a list

print("----- Exercise 8: L2-norm of a list -----")

def norm(lst):
    return math.sqrt(sum(x**2 for x in lst))

print(norm([1,2,2]))  # 3.0

# Exercise 9: Check if array is monotonic

print("----- Exercise 9: Check if array is monotonic -----")
def is_mono(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

print(is_mono([7,6,5,5,2,0]))  # True
print(is_mono([2,3,3,3]))      # True
print(is_mono([1,2,0,4]))      # False


# Exercise 10: Longest word in a list

print("----- Exercise 10: Longest word in a list -----")

def longest_word(lst):
    return max(lst, key=len)

print(longest_word(["cat", "elephant", "dog"]))  # elephant

# Exercise 11: Separate integers and strings
print("----- Exercise 11: Separate integers and strings -----")

def separate_types(lst):
    ints = [x for x in lst if isinstance(x, int)]
    strs = [x for x in lst if isinstance(x, str)]
    return ints, strs

print(separate_types([1,'a',2,'b',3, c, 4]))  

# Exercise 12: Check if palindrome
print("----- Exercise 12: Check if palindrome -----")

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('radar'))  
print(is_palindrome('John'))  

# Exercise 13: Words longer than k
print("----- Exercise 13: Words longer than k -----")

def sum_over_k(sentence, k):
    return sum(1 for word in sentence.split() if len(word) > k)

sentence = 'Do or do not there is no try'
print(sum_over_k(sentence, 2)) 

# Exercise 14: Average value in dictionary
print("----- Exercise 14: Average value in dictionary -----")

def dict_avg(d):
    return sum(d.values()) / len(d)

print(dict_avg({'a': 1,'b':2,'c':8,'d': 1})) 

# Exercise 15: Common divisors
print("----- Exercise 15: Common divisors -----")
def common_divisors(a, b):
    divisors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    return divisors
# Exercise 16: Check if prime
print("----- Exercise 16: Check if prime -----")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Exercise 17: Print elements if index and value are even
print("----- Exercise 17: Print elements if index and value are even -----")
def weird_print(lst):
    return [lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 == 0]

print(weird_print([1,2,2,3,4,5]))  # [2,4]

# Exercise 18: Count types of keyword arguments
print("----- Exercise 18: Count types of keyword arguments -----")

def type_count(**kwargs):
    counts = {}
    for key, value in kwargs.items():
        t = type(value).__name__   
        counts[t] = counts.get(t, 0) + 1
    return counts

print(type_count(a=1, b='string', c=1.0, d=True, e=False))
# Output: {'int': 1, 'str': 1, 'float': 1, 'bool': 2}

# Exercise 19: Mimic .split()
print("----- Exercise 19: Mimic .split() -----")

def my_split(s, sep=None):
    result = []
    word = ''
    for c in s:
        if c == sep or (sep is None and c.isspace()):
            if word:
                result.append(word)
                word = ''
        else:
            word += c
    if word:
        result.append(word)
    return result

print(my_split("Do or do not"))          # ['Do','or','do','not']
print(my_split("a,b,c", sep=','))        # ['a','b','c']

# Exercise 20: Convert string to password format
print("----- Exercise 20: Convert string to password format -----")


def to_password(s):
    return '*' * len(s)

print(to_password("Azerty123"))  # **********
