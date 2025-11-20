import random
import sys
import os

def get_words_from_file(file_path):
    """
    Reads a file and returns a list of words
    """
    try:
        with open(file_path, "r") as f:
            content = f.read()  
        words = content.split()  
        return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
        sys.exit(1)  

# Step: Generate random sentence 
def get_random_sentence(length):
    """
    Generate a random sentence of a given length
    """
    words = get_words_from_file("words.txt")  
    sentence_words = [random.choice(words) for _ in range(length)]   
    sentence = " ".join(sentence_words).lower()
    return sentence  

# Step : Main function 

def main():
    print("Welcome! This program generates a random sentence.")

    user_input = input("Enter sentence length (2-20): ")
    
    # Input validation 
    if not user_input.isdigit():
        print("Invalid input! Not a number. ")
        sys.exit(1)
    
    length = int(user_input)
    if length < 2 or length > 20:
        print("Invalid input! Number must be between 2 and 20. ")
        sys.exit(1)
    
    sentence = get_random_sentence(length)
    print("Generated sentence:")
    print(sentence)

# Run the program
if __name__ == "__main__":
    main()
