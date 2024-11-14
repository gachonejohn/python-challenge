# Choose a secret number. prompt the user to guess your secret number. allow the user to guess
# a maximum of three times and give him a feedback of whether the guess is right or wrong.


def secret_num():
    secret_number = 23

    num = int(input("Guess the number: "))

    if num == secret_number:
        print("Correct!")
    elif num > secret_number:
        print("Too high!")
    else:
        print("Too low!")

secret_num()
# adding maximum number of trials

