# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old,
# except use f-strings instead of the + operator to print the resulting output message.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

year = 100 - age
print(f"Hi {name}, your will turn 100 years after {year} years.") #changing the years to the actual year

