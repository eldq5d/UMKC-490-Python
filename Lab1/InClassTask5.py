# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
# Hint: use functions.
# heightinp= int(input("Enter the height of the board: "))
# widthinp= int(input("Enter the width of the board: "))
# board_draw(heightinp,widthinp)

heightInp = int(input("Enter the height of your board: "))
widthInp = int(input("Enter the width of your board: "))
x = 1
while x <= heightInp:
    print("---  " * widthInp)
    print("|   " * (widthInp + 1))
    x += 1
print ("---  " * widthInp)
