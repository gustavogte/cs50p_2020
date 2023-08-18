# While forever
while True:
    # Get user input
    fuel = input("Fraction: ")
    try:
        # Try to split the fuel
        numerator, denominator = fuel.split(sep="/")
        # Convert into integers
        new_numerator = int(numerator)
        new_denominator = int(denominator)
        # Calculate Percentage
        f = new_numerator / new_denominator
        # Check if its less than 1 and stop the loop
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
# Multiply percentage by 100
p = int(f * 100)
# Check if percentage is less than 1, print E
if p <= 1:
    print("E")
# Check if percentage is greater than 99, pring F
elif p >= 99:
    print("F")
# Otherwise, print the %
else:
    print(f"{p}%")