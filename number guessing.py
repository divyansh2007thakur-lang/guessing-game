import random


DIFFICULTY_RANGES = {
    "easy": 50,
    "medium": 100,
    "hard": 200,
}

print("Choose a difficulty: easy, medium, or hard.")
while True:
    difficulty = input("Difficulty: ").strip().lower()
    if difficulty in DIFFICULTY_RANGES:
        break
    print("Please choose easy, medium, or hard.")

max_number = DIFFICULTY_RANGES[difficulty]
secret_number = random.randint(1, max_number)
attempts = 0

print(f"I'm thinking of a number between 1 and {max_number}.")

while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low. Try again!")
    elif guess > secret_number:
        print("Too high. Try again!")
    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break