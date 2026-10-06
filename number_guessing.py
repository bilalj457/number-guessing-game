import random


def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\nI have chosen a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")


def main():
    print("===== GuessIt Number Game =====")

    while True:
        play_game()

        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
