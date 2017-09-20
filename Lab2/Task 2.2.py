# With any given number n, Write a program to generate a dictionary that contains (k, k*k).
# Print the dictionary generated and the series should include both 1 and k.

n = int(input("Enter an integer to create a dictionary: "))
dictionary1 = {}
for i in range(1, n+1):
    dictionary1[i] = i*i
    i += 1
print(dictionary1)
