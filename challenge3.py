# write as a simple program that prompts the user to enter two numbers.
# Then, configure the program to perform various arithmetic operations on the two numbers,
# including addition, subtraction, multiplication, division,
# and exponentiation and print the results.


#promting the user for the inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#addition
print(f"The sum of {num1} and {num2} is: {num1+num2}")

#subtraction
print(f"The difference of {num1} and {num2} is: {num1-num2}")

#multiplication
print(f"The product of {num1} and {num2} is: {num1*num2}")

#division
print(f"{num1} divided by {num2} is: {num1/num2}")

#expontiation
print(f"The exponent of {num1}  and {num2} is: {num1**num2}")