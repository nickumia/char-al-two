##  Get Characters that appear at least two times
#   Developer: nickumia
#   04.06.2021

import sys
import time

VERBOSE = False

# Input string to test
input_string = input("Enter a character string: ")

# Start time
start = time.time()

# Dictionary to hold frequence count
# Only the alphabet characters are supported
char_frequency = {key:0 for key in 
    [chr(i) for i in range(ord('a'), ord('z')+1)]}


for char in input_string:
    try:
        char_frequency[char.lower()] += 1
    except KeyError:
        print("Input string contains non-supported characters.  " + 
            "Try again with only characters in the range of [a-z].")


char_al_two = []
for char in char_frequency:
    if char_frequency[char] >= 2:
        char_al_two.append(char)
        if VERBOSE:
            print("Character \'%s\' occurred %d times" % (char, char_frequency[char]))

# End time
end = time.time()

print(char_al_two)
print(sys.getsizeof(char_al_two))
print(end-start)

# -> Result list
# -> Memory usage in terms of bytes
#       THe memory usage is the size of the dictionary and
#       optionally the size of the result list
# -> Time
#       The time cost is time it costs to visit every character
#       in the input string. O(n) where n = number of characters.