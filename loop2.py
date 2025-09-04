# Program to calculate the n-th power of a given number

base = float(input("Enter the base number: "))    # convert to float
exponent = int(input("Enter the exponent number: "))  # convert to int

result = 1  # start with 1

# Loop to multiply base exponent times
for i in range(abs(exponent)):
    result *= base

# If exponent is negative, take reciprocal
if exponent < 0:
    result = 1 / result

print(f"{base} raised to the power of {exponent} is {result}")
