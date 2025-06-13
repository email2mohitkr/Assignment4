
'''
Task 1:
 Read a File and Handle Errors
Problem Statement:  Write a Python program that:

1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.


'''
from typing import final

try:
    with open('Simple.txt','r') as myfile1:
        print('Reading file content :')
        print(myfile1.read())
        #print(myfile1.readline())
except FileNotFoundError:
    print('Error: The File Simple.txt was not found')




