"""Number Guessing Game & Word Counter (InternCircle Project 2).

A terminal program with two tools behind a start menu:
  1) A number guessing game with an attempt counter, score and best score.
  2) A word counter that reads a text file and reports the most common words.
"""

import random
import string
from collections import Counter

# ---------- Game rules (change them here) ----------
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 7
START_SCORE = 100   # score for a first-guess win
PENALTY = 10        # points lost for every extra guess
TOP_N = 10          # how many words the counter shows
DEFAULT_FILE = "sample.txt"


# ---------- Number guessing game ----------

def parse_guess(text):
    """Return the guess as an int, or None (with a message) if it is invalid."""
    text = text.strip()
    if text == "":
        print("Please type a number; empty input is not a guess.")
        return None
    try:
        guess = int(text)
    except ValueError:
        print("That is not a whole number. Try something like 42.")
        return None
    if not MIN_NUMBER <= guess <= MAX_NUMBER:
        print(f"Your guess must be between {MIN_NUMBER} and {MAX_NUMBER}.")
        return None
    return guess


def calculate_score(attempts_used):
    """Score for a win: 100 minus 10 points for every guess after the first."""
    return START_SCORE - PENALTY * (attempts_used - 1)


def play_round():
    """Play one round and return the score (0 if the player runs out of attempts)."""
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)  # picked once per round
    attempts_used = 0
    print(f"\nI am thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"You have {MAX_ATTEMPTS} attempts.")

    while attempts_used < MAX_ATTEMPTS:
        remaining = MAX_ATTEMPTS - attempts_used
        guess = parse_guess(input(f"Guess ({remaining} left): "))
        if guess is None:
            continue  # invalid input does not use up an attempt
        attempts_used += 1

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            score = calculate_score(attempts_used)
            print(f"Correct! You got it in {attempts_used} attempt(s).")
            print(f"Score this round: {score}")
            return score

    print(f"Out of attempts! The number was {secret}.")
    print(f"Attempts used: {attempts_used}. Score this round: 0")
    return 0


def ask_yes_no(prompt):
    """Keep asking until the user answers y or n; return True for yes."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def play_game():
    """Run rounds until the player stops, tracking the best score."""
    best_score = 0
    while True:
        score = play_round()
        best_score = max(best_score, score)
        print(f"Best score so far: {best_score}")
        if not ask_yes_no("Play again? (y/n): "):
            break


# ---------- Word counter ----------

def count_words(path):
    """Return a Counter of words in the file, or None if it cannot be read."""
    try:
        with open(path, encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"File not found: '{path}'. Check the name and folder, then try again.")
        return None
    except (UnicodeDecodeError, OSError):
        print(f"Sorry, '{path}' could not be read as a UTF-8 text file.")
        return None

    text = text.translate(str.maketrans("", "", string.punctuation))
    return Counter(text.split())


def show_word_report(counts):
    """Print totals and the most common words in neat columns."""
    total = sum(counts.values())
    if total == 0:
        print("The file is empty (no words found).")
        return
    print(f"\nTotal words : {total}")
    print(f"Unique words: {len(counts)}")
    print(f"\n{'Rank':<6}{'Word':<15}{'Count':>6}")
    print("-" * 27)
    for rank, (word, count) in enumerate(counts.most_common(TOP_N), start=1):
        print(f"{rank:<6}{word:<15}{count:>6}")
    print("\nNote: common words like 'the' and 'and' usually dominate the top of the list.")


def run_word_counter():
    """Ask for a file name and show its word statistics."""
    name = input(f"File name (press Enter for {DEFAULT_FILE}): ").strip() or DEFAULT_FILE
    counts = count_words(name)
    if counts is not None:
        show_word_report(counts)


# ---------- Start menu ----------

def main():
    """Show the start menu until the user chooses Quit."""
    while True:
        print("\n===== Game & Word Counter =====")
        print("1) Play the number guessing game")
        print("2) Count words in a file")
        print("3) Quit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            run_word_counter()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
