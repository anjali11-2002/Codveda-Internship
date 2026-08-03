import random

print("=" * 40)
print("      NUMBER GUESSING GAME")
print("=" * 40)

while True:

    secret_num = random.randint(1, 100)
    attempts = 7
    guessed = False

    print("\nI have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.")

    while attempts > 0:

        try:
            guess = int(input(f"\nAttempt {8 - attempts}/7 - Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_num:
                print("Too Low!")

            elif guess > secret_num:
                print("Too High!")

            else:
                used_attempts = 8 - attempts
                print(f"\n🎉 Congratulations! You guessed the number {secret_num}.")
                print(f"You guessed it in {used_attempts} attempt(s).")
                guessed = True
                break

            attempts -= 1
            print(f"Attempts Left: {attempts}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if not guessed:
        print(f"\n😢 Game Over! The correct number was {secret_num}.")

    while True:
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()

        if play_again in ("y", "yes"):
            break

        elif play_again in ("n", "no"):
            print("\nThanks for playing! Goodbye.")
            exit()

        else:
            print("Invalid choice! Please enter y/yes or n/no.")
            