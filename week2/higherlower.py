import random

correct = random.randint(0, 100)

guess = -1  # init to unreachable number

number_of_guesses = 0

while guess != correct:
    try:
        guess = int(input("Enter your guess: "))
        number_of_guesses += 1
    except ValueError:
        print("Please enter a number")
        continue

    if guess < correct:
        print("Too low")
    elif guess > correct:
        print("Too high")

print(
    f"Correct! The number was: {correct}, you took {number_of_guesses} time(s) to guess right."
)
