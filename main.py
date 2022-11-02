import random
import hangman_words
import hangman_art

from hangman_art import logo

stages = hangman_art.stages

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

lives = 6

guessed_letters = {}

while '_' in display:
    # clear()
    print(logo, '\n\n')
    print(stages[lives], end='\n')
    print(' '.join(display), end='\n\n')
    print('you\'ve guessed these letters: ', end='')
    print(guessed_letters)
    print('\n')
    guess = input("Guess a letter: ").lower()
    guessed_letters = list(guessed_letters)
    guessed_letters += guess
    guessed_letters = set(guessed_letters)
    print('\n')
    if (guess in display):
        pass
    elif (guess in chosen_word):
        for i in range(word_length):
            if (guess == chosen_word[i]):
                display[i] = guess
    else:
        lives -= 1
        if (lives == 0):
            print(stages[lives], end='\n')
            print('\nyou lose')
            print(f'the word was {chosen_word}\n')
            break
else:
    print('\nyou win')
