# Write a program that accepts a sentence as input and remove duplicate words.
# Sort them alphanumerically and print it

user = input("Enter a sentence: ")
alpha = 'abcdefghijklmnopqrstuvwxyz '
for s in user:
    if s not in alpha:
        user = user.replace(s, '')
secondSet = user.split(" ")
thirdSet = set(secondSet)
finalSet = sorted(thirdSet)
print(finalSet)
