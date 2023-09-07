Que. Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

INPUT:
# Define a function named 'most_frequent' that takes an 'input_string' as its parameter.
def most_frequent(input_string):
    # Remove spaces from the input string.
    input_string = input_string.replace(" ", "")
    
    # Create an empty dictionary to store letter frequencies.
    letter_frequency = {}
    
    # Iterate through each character in the input string.
    for letter in input_string:
        # Check if the character is an alphabetic letter.
        if letter.isalpha():
            # If the letter is already in the dictionary, increment its frequency.
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            # If the letter is not in the dictionary, add it with a frequency of 1.
            else:
                letter_frequency[letter] = 1
    
    # Sort the letter frequencies in descending order.
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Iterate through the sorted frequencies and print each letter and its frequency.
    for letter, frequency in sorted_frequency:
        print(f"{letter}: {frequency}")

# Get user input and call the 'most_frequent' function with the input.
user_input = input("Please enter a string: ")
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
