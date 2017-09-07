# Write a Python program to check if a string contains all letters of the alphabet

string = input("Enter a word or sentence: ")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
charList = list(string)
if (all(i in charList for i in alphabet)):
    print("All letters of the alphabet are present!")
else:
    print("All letters of the alphabet are NOT present.")
