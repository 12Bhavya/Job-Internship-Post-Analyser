import random

lines = open('file_name.csv').readlines() # Add file name here
random.shuffle(lines)
open('shuffled_file_name.csv', 'w').writelines(lines) # Output file name here
