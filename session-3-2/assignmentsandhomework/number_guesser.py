# number_guesser.py
# Guessing Game (while loop + random + hints + guess counter)

import random

# 1) Computer picks random number 1-100
secret = random.randint(1, 100)

print("=" * 40)
print("NUMBER GUESSER (1 to 100)")
print("=" * 40)
print("I picked a number between 1 and 100.")
print("Try to guess it!\n")

# 4) Count number of guesses
guesses = 0

# 2) User guesses (while loop)
while True:
    user_input = input("Enter your guess (1-100): ").strip()

    # Basic input validation
    if not user_input.isdigit():
        print("Please enter a whole number.\n")
        continue

    guess = int(user_input)

    if guess < 1 or guess > 100:
        print("Your guess must be between 1 and 100.\n")
        continue

    guesses += 1

    # 3) Give hints
    if guess > secret:
        print("Too high! Try again.\n")
    elif guess < secret:
        print("Too low! Try again.\n")
    else:
        # 6) Correct message + 5) stop game (break)
        print(f"Correct! You took {guesses} guesses.")
        break
