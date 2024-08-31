import random

with open('words.txt', 'r') as file:
    words = file.read().splitlines()

random_word = random.choice(words)

availableGuesses = len(random_word)

totalGuesses = 0

secretWord = ""

for i in range(availableGuesses):
    secretWord = secretWord + "*"

print("====Welcome to Guessing The Word game!====")
print("Here is the word you have to guess:")
print(secretWord)
print("You have ", availableGuesses, " chances to guess the word!")

while totalGuesses < availableGuesses and secretWord != random_word:
    totalGuesses += 1
    letter = input("Enter a letter:")
    if letter not in random_word:
        print("Try again! You have ", availableGuesses - totalGuesses, " changes to guess the word.")
    else:
        idx = 0
        for alphabet in random_word:
            if alphabet == letter:
                if idx == (len(random_word) - 1):
                    secretWord = secretWord[:idx] + letter
                    print(secretWord)
                    if secretWord == random_word:
                        break
                    print("You have ", availableGuesses - totalGuesses, " changes to guess the word.")
                else:
                    secretWord = secretWord[:idx] + letter + secretWord[idx + 1:]
                    print(secretWord)
                    if secretWord == random_word:
                        break
                    print("You have ", availableGuesses - totalGuesses, " changes to guess the word.")

            idx += 1

if secretWord == random_word and totalGuesses < availableGuesses:
    print("Congrats! You won!")
else:
    print("The correct word is: ", random_word, ". Better lucky next time!")




