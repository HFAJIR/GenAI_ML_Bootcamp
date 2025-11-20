import string
import re

# Part I: Text Analysis
class Text:
    def __init__(self, text):
        self.text = text

    # Step 2: Word Frequency
    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return f"The word '{word}' is not found in the text."
        return count

    # Step 3: Most Common Word
    def most_common_word(self):
        words = self.text.split()
        if not words:
            return "Text is empty."
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        most_common = max(freq, key=freq.get)
        return most_common

    # Step 4: Unique Words
    def unique_words(self):
        words = self.text.split()
        return list(set(words))

    # Step 5: Create instance from file
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return cls(content)


# Part II: Text Modification
class TextModification(Text):
    
    # Step 7: Remove punctuation
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        self.text = self.text.translate(translator)
        return self.text

    # Step 8: Remove stop words
    def remove_stop_words(self):
        stop_words = {
            "a", "the", "is", "in", "at", "of", "on", "and", "or", "an", "to", "for", "with", "by"
        }
        words = self.text.split()
        filtered_words = [w for w in words if w.lower() not in stop_words]
        self.text = ' '.join(filtered_words)
        return self.text

    # Step 9: Remove special characters
    def remove_special_characters(self):
        self.text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return self.text

# Example usage
if __name__ == "__main__":
    my_text = Text("Hello world! This is a test. Hello again.")
    print("Frequency of 'Hello':", my_text.word_frequency("Hello"))
    print("Most common word:", my_text.most_common_word())
    print("Unique words:", my_text.unique_words())   # use set to avoid duplicates

    # Part II: From a file (uncomment and use a real file path)
    # text_from_file = Text.from_file("sample.txt")
    # print(text_from_file.text)

    # Text modification
    mod_text = TextModification("Hello, world! This is a test #2025.")
    print("Without punctuation:", mod_text.remove_punctuation())
    print("Without stop words:", mod_text.remove_stop_words())
    print("Without special characters:", mod_text.remove_special_characters())