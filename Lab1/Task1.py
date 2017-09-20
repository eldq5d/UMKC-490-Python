# Read a file which includes at least two paragraphs.
# Calculate the word frequency for each word in the file. The steps to do so are:
# 1. Split the words in the file
# 2. Use a loop to iterate over the words.
# 3. Add the first word to the file, put the value 1
# 4. Add the second word to the file, put the value 1.
# 5. If you faced with a word that you have already added to the file, just update the value
# 6. Finally, you will have a file which includes all the words with their counts,
# ex: {“Is”: 5, “politics”:3, “country”:1, ...}

fileName = input("What file are the paragraphs in?: ")
infile = open(fileName, 'r')
line = infile.readline()
listOfWords = []
freqOfWords = []
while line != "":
    line = line.strip()
    listOfWords.extend(line.split(" "))
    line = infile.readline()
for w in listOfWords:
    freqOfWords.append(listOfWords.count(w))
newList = list(zip(listOfWords, freqOfWords))
finalList = set(newList)
print(finalList)
print(newList)
