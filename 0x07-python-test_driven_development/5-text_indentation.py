#!/usr/bin/python
"""
This module contains a ``text_indentation`` function
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.' '?' or ':'

    Args:
        text (str): text to be formatted

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize string builder for efficiency
    result = []
    sentence = ""

    # Iterate over each character
    for char in text:
        sentence += char

    # Checks for punctuations
        if char in ".:?":
            result.append(sentence.strip()) 
            sentence = ''

    # Print any remaining part of the text (if it doesn't end with punctuation)
    if char:
        result.append(sentence.strip())

    # Print the formatted text
    print("\n\n".join(result), end='')
