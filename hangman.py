import random

HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
========''', '''
  +---+
  O   |
      |
      |
      |
========''', '''
  +---+
  O   |
  |   |
      |
      |
========''', '''
  +---+
  O   |
 /|   |
      |
      |
========''', '''
  +---+
  O   |
 /|\  |
      |
      |
========''', '''
  +---+
  O   |
 /|\  |
 /    |
      |
========''', '''
  +---+
  O   |
 /|\  |
 / \  |
      |
========''']

word_list = ['apple', 'banana', 'mango', 'orange', 'watermelon', 'grapes', 'strawberry', 'pineapple', 'peach', 'cherry', 'plum', 'kiwi', 'papaya', 'guava', 'blueberry']
lives=6
chosen_word=random.choice(word_list)
display=[]
for i in range(len(chosen_word)): 
      display += '_'

print(display)
game_over=False
while not game_over:
     print(HANGMAN_PICS[6-lives])
     guessed_letter=input("Guess a letter: ").lower()

     for position in range(len(chosen_word)):
           letter =chosen_word [position]
           if letter==guessed_letter:
                display [position] = guessed_letter

     print(display)

     if guessed_letter not in chosen_word:
          lives-=1
          print(f"Incorrect! You have {lives} lives left.")
          if lives == 0:
             game_over = True
             print("You lose!!")

     if '_' not in display:
          game_over=True
          print("You win !!")

print("Thanks for playing!")