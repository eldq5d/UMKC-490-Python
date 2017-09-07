# Write a Python program to check if a string contains all letters of the alphabet

# infile = input("Give me a sentence: ")
# listOfWords = infile.split(" ")
# freqOfWords = []
# while line != "":
# for w in listOfWords:
    # freqOfWords.append(listOfWords.count(w))
# print(listOfWords)
# print(freqOfWords)

# newList = list(zip(listOfWords, freqOfWords))
# print(newList)
string = input("Enter a word or sentence: ")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
charList = list(string)
print(all(i in charList for i in alphabet))
