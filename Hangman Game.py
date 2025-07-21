import random

# Predefined list of words
words = ["apple", "banana", "orange", "grapes", "mango"]

# Select a random word
chosen_word = random.choice(words)
word_length = len(chosen_word)

# Variables
guessed_letters = []
attempts_left = 6

# Create a display version with underscores
display = ["_"] * word_length

print("🎮 Welcome to Hangman Game!")
print("Guess the word by entering one letter at a time.")

# Game loop
while attempts_left > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print(f"Attempts left: {attempts_left}")
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
    else:
        print("❌ Wrong guess.")
        attempts_left -= 1

# Final result
if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)
