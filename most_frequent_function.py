Que. Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

INPUT:
def most_frequent(input_string):
    input_string = input_string.replace(" ", "")
    # Initializing an empty dictionary to store letter's frequencies
    letter_frequency = {}
    # Performimg for i in range and if/else
    for letter in input_string:
        if letter.isalpha():
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1
    # Sorting the dictionary by values (i.e, frequency) in descending order
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)
    for letter, frequency in sorted_frequency:
        print(f"{letter}: {frequency}")
user_input = input("Please enter a string: ")
# Calling function with the user's input
most_frequent(user_input)


OUTPUT:
Please enter a string: Mississippi
i: 4
s: 4
p: 2
M: 1

# Other input tries:
Please enter a string: Samsung
S: 1
a: 1
m: 1
s: 1
u: 1
n: 1
g: 1
