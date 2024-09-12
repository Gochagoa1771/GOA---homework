# Task 1: Format a String
name = input("Enter your name: ")
age = input("Enter your age: ")
formatted_string = "Hello, {}! You are {} years old.".format(name, age)
print(formatted_string)

# Task 2: Join a List of Strings
words = ["Python", "is", "fun"]
joined_string = " ".join(words)
print(joined_string)

# Task 3: Split a String
sentence = input("Enter a sentence: ")
words_list = sentence.split()
print(words_list)

# Task 4: Replace Substrings
sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
modified_sentence = sentence.replace(old_word, new_word)
print(modified_sentence)

# Task 5: Convert to Lowercase
mixed_case_string = input("Enter a mixed-case string: ")
lowercase_string = mixed_case_string.lower()
print(lowercase_string)

# Task 6: Convert to Uppercase
sentence = input("Enter a sentence: ")
uppercase_sentence = sentence.upper()
print(uppercase_sentence)