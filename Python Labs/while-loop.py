import random
print("Welcome to guess the number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,100)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 100: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
    