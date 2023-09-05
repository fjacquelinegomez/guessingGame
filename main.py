import random 
import check_input

def main():

    randomNumber = random.randint(1,100)
    print("--Guessing Game--")
    numberGuessed = check_input.get_int_range("Im thinking of a number. Make a guess (1-100): ", 1, 100)
    count = 1
    while numberGuessed != randomNumber:
        if (numberGuessed < randomNumber):
            numberGuessed = check_input.get_positive_int("Too low! Guess again (1-100): ")
            count += 1
        elif (numberGuessed > randomNumber):
            numberGuessed = check_input.get_positive_int("Too high! Guess again (1-100): ")
            count += 1
        else:
            numberGuessed = check_input.get_int("Invalid. Guess again (1-100): ")
    print("Yay. You got in ", count,"tries.")

main()