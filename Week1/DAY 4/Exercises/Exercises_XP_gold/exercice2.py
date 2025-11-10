

def sum_x_variations(x: int) -> int:
    """Return the sum of X + XX + XXX + XXXX for a given integer X."""
    str_x = str(x)  # Convert the integer to a string for concatenation
    total = 0
    for i in range(1, 5):  # Loop from 1 to 4 to create X, XX, XXX, XXXX
        term = int(str_x * i)  # Create the term by repeating the string and convert back to int
        total += term  # Add the term to the total
    return total
# -------- Main program --------
x = int(input("Enter an integer X: ").strip())
result = sum_x_variations(x)
print(result)

