
#Challenge 2: Retirement Eligibility Checker
def longest_word(sentence):
    words = sentence.split()  # Split the sentence into words
    longest = ""  # Initialize the longest word variable

    for word in words:
        if len(word) > len(longest):
            longest = word  # Update longest if current word is longer

    return longest

print(longest_word("Margaret's toy is a pretty doll."))  
print(longest_word("A thing of beauty is a joy forever."))  
print(longest_word("Forgetfulness is by all means powerless!"))  

