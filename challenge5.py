# Write a Python program that prompts the user to enter a numerical grade between 0 and 100,
# and then prints the corresponding congratulatory message based on the following grading scale:
#            90 and above: good job ( >=95 excellent )
#             80 to 89: well done
#             70 to 79: keep it up
#             60 to 69: average
#             Below 60: needs improvement

grade = int(input("Enter your grade: "))

if 90 <= grade <= 100:
    print("Good job")
elif 80 <= grade <= 89:
    print("Well done")
elif 70 <= grade <= 79:
    print("keep it up")
elif 60 <= grade <= 69:
    print("Average")
elif grade < 60:
    print("Needs improvement")
else:
    print("Invalid input; Grade should be between 0 and 100")

