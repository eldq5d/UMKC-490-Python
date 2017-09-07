# Write a Python program to find those numbers which are
# divisible by 5 and multiple of 2, between 700 and 1700

for i in range(700, 1700+1):
    if i%5 == 0:
        if i%2 == 0:
            print(i)
            i += i
        else:
            i += i
    else:
        i += i
