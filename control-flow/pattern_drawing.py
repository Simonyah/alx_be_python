# pattern_drawing.py

# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle each row
while row < size:
    # Use a for loop to print asterisks in the row
    for col in range(size):
        print("*", end="")  # Print without newline
    print()  # Move to the next line after the row is printed
    row += 1
