#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#This program defines two functions that take a string as input. The first function, alternate_case, converts the characters in the string to alternate uppercase 
#and lowercase letters based on their index. The second function,
# alternate_word_case, converts the words in the string to alternate uppercase and lowercase letters based on their index.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def alternate_case(string):  # Define a function that takes a string as input
    return "".join(
        [
            string[
                i
            ].upper()  # If the index is even, convert the character to uppercase
            # If the index is odd, convert the character to lowercase
            if i % 2 == 0 else string[i].lower()
            for i in range(len(string))
        ]
    )  # Iterate over each character in the string


def alternate_word_case(string):  # Define a function that takes a string as input
    words = string.split()  # Split the string into words
    return " ".join(
        [
            # If the index is even, convert the word to lowercase
            words[i].lower()
            # If the index is odd, convert the word to uppercase
            if i % 2 == 0 else words[i].upper()
            for i in range(len(words))
        ]
    )  # Iterate over each word in the list


string = "I am learning to code:\n"  # Define a string variable
print(alternate_case(string))  # Call the function and print the result
string = "I am learning to code:\n"  # Define a string variable
print(alternate_word_case(string))  # Call the function and print the result
