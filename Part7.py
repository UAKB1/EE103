import random

secret_number = random.randint(1, 10)

for attempt in range(1, 4):
    guess = int(input(f"Try {attempt}/3 - guess the secret number (1-10): "))
    correct = guess == secret_number
    print(correct)

    if correct:
        print("Correct!")
        break
    elif guess < secret_number:
        print("Too low. Go up!")
    else:
        print("Too high. Go down!")
else:
    print(f"No tries left. The secret number was {secret_number}.")
