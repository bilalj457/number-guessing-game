# GuessIt - Number Guessing Game

GuessIt is a simple number guessing game made with Python.

The computer chooses a random number between 1 and 100, and the player tries to guess it.

## Features

- Random number from 1 to 100
- Too high / too low hints
- Counts attempts
- Handles invalid input
- Play again option
- Simple terminal interface

## Technologies

- Python 3
- `random` module
- No external libraries

## Project Structure

```text
guessit-number-game/
├── number_guessing.py
├── README.md
└── .gitignore
```

## How to Run

```bash
git clone https://github.com/bilalj457/guessit-number-game.git
cd guessit-number-game
python number_guessing.py
```

## Example

```text
===== GuessIt Number Game =====

I have chosen a number between 1 and 100.
Try to guess it!

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Correct! You guessed the number in 3 attempts.

Do you want to play again? (yes/no): no
Thanks for playing!
```

## What I Learned

- Functions
- Variables
- `while` loops
- `if`, `elif`, and `else`
- User input
- `try` and `except`
- The `random` module
- Comparisons
- Counters

## Future Improvements

- Difficulty levels
- Maximum attempts
- Score system
- Best score
- Hints
- Different number ranges

## Author

Bilal J

GitHub: [@bilalj457](https://github.com/bilalj457)
