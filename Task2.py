'''
Task 2:
Write and Append Data to a File

Problem Statement: Write a Python program that:

1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads a
'''
try:
    with open('output.txt','w') as fileWrite:
        str=   input('Enter text to write to the file :')
        fileWrite.write(str + '\n')
        print('Data successfully write to output.txt \n\n')
except FileNotFoundError:
    print('File not found')

try:
    with open('output.txt','a+') as fileWrite:
        str1=   input('Enter additional text to apend :')
        fileWrite.write(str1 + '\n')
        print('Data successfully append \n\n')

except FileNotFoundError:
    print('File not found')

try:
    with open('output.txt','r') as fileRead:
        print('Final content of output.txt')
        print( fileRead.read())


except FileNotFoundError:
    print('File not found')

