import random

correct = random.randint(0, 99)

guess = None

number_of_guesses = 0

while guess != correct:
    try:
        guess = int(input("Enter your guess: "))
        number_of_guesses += 1
    except ValueError:
        print("Please enter a number")
        continue
    except KeyboardInterrupt:
        print(f"\nExiting game, the number was {correct}...")
        exit(1)

    if guess < correct:
        print("Too low")
    elif guess > correct:
        print("Too high")

print(
    f"Correct! The number was: {correct}, you took {number_of_guesses} time(s) to guess right."
)
