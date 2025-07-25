import random

# Hangman ASCII stages
stages = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |
     |
     |
     |
    --------
    """
]

# Dictionary with words and hints
words_with_hints = {
    "apple": "A common red or green fruit",
    "banana": "A yellow fruit that's long and curved",
    "orange": "A fruit and also a color",
    "grapes": "Small round fruits that grow in bunches",
    "mango": "A sweet tropical fruit, king of fruits"
    "carrot" "An orange vegetable rabbits love",
    "python": "A programming language and a snake",
    "school": "A place where students go to learn",
    "pizza": "A round fast food loved by many",
    "guitar": "A musical instrument with strings"
}

def play_game():
    # Pick word and hint
    chosen_word, hint = random.choice(list(words_with_hints.items()))
    word_length = len(chosen_word)
    guessed_letters = []
    attempts_left = 6
    display = ["_"] * word_length

    print("🎮 Welcome to Hangman Game!")
    print(f"💡 Hint: {hint}")
    print("Guess the word by entering one letter at a time.")

    while attempts_left > 0 and "_" in display:
        print(stages[6 - attempts_left])
        print("Word:", " ".join(display))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("✅ Good guess!\n")
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = guess
        else:
            print("❌ Wrong guess.\n")
            attempts_left -= 1

    # Final result
    print(stages[6 - attempts_left])
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", chosen_word)
    else:
        print("💀 Game Over! The word was:", chosen_word)

# Start menu
while True:
    play_game()
    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if again != 'yes':
        print("👋 Thanks for playing Hangman. Goodbye!")
        break
