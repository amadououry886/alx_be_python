# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the row
    for _ in range(size):
        print("*", end="")  # Print asterisks side by side
    print()  # Move to the next line after each row
    row += 1

