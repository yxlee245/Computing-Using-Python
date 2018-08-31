# Palindrome tester
import string

original_str = input('Input a string: ')
modified_str = original_str.lower()

bad_chars = string.whitespace + string.punctuation

for char in modified_str:
    if char in bad_chars:   # remove bad characters
        modified_str = modified_str.replace(char, '')

if modified_str == modified_str[::-1]:    # it is a palindrome
    print(\
    'The original string is: {}\n\
    the modified string is: {}\n\
    the reversal is: {}\n\
    String is a palindrome'.format(original_str, modified_str,
    modified_str[::-1]))
else:
    print(\
    'The original string is: {}\n\
    the modified string is: {}\n\
    the reversal is: {}\n\
    String is a not a palindrome'.format(original_str,
    modified_str, modified_str[::-1]))