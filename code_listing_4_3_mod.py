# Our implementation of the find function. Prints the index where
# the target is found; a failure message, if it isn't found.
# This version only searches for a single character.

river = 'Mississippi'
target = input('Input a character to find: ')
count_int = 0
for index, letter in enumerate(river):    # for each index
    if letter == target:    # check if the target is found
        print('Letter found at index:', index)    # if so, print the index
        count_int += 1
        # break
    else:
        continue

if count_int == 0:
    print('Letter', target, 'not found in', river)