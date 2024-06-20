from random import choice
from hangman_art import drawing
from replit import clear
import time

def main():
  playing_status = True
  while playing_status == True:
    is_endgame = False
    global chosen_word
    chosen_word = word_select()
    print(chosen_word)
    guess_count = 0
    while not is_endgame:
      guess = user_guess()
      guess_count = guess_check(chosen_word,guess,guess_count)
      is_endgame = display(chosen_word,guess_count)
    user_choice()

def welcome_message():
  print("--------------------------")
  print("|   Welcome to Hangman   |")
  print("--------------------------\n")
  print("I'm choosing a word... Okay I've got one\n")

def word_select():
  with open("english_dictionary.txt", mode="r") as words:
      word_list = words.readlines()
  chosen_word = choice(word_list).strip()
  length= len(chosen_word)
  print(f"The word is {length} letters long\n")
  display(chosen_word,guess_count)
  return chosen_word

def user_guess():
  while True:
    guess = input("\nPlease enter your guess:")
    if len(guess) == 1 and guess.isalpha():
      return guess.lower()
    else:
      print("That is not a valid input. Try Again!")

def guess_check(word,guess,count):
  if guess in word and guess not in guessed_letters:
    print(f"\nNice work! {guess.upper()} is in the word!\n")
    guessed_letters.append(guess)
    return count+1
  elif guess not in word and guess not in wrong_letters:
    print(f"\nOh no! There is no {guess.upper()} in this word!\n")
    wrong_letters.append(guess)
    drawing(len(wrong_letters),wrong_letters)
    return count+1
  else:
    print("\nYou already guessed that letter! Try again!")
    return count

def display(chosen_word,count):
  dash = "___ "
  sentence = []
  is_solved = False
  is_lost = False
  for letter in chosen_word:
    if letter in guessed_letters:
      sentence.append(letter)
      sentence.append(" ")
    else:
      sentence.append(dash)
  print("".join(sentence))
  if count > 0:
    is_solved = win_check(dash,sentence,count)
    is_lost = lose_check()
  return is_solved or is_lost

def lose_check():
  if len(wrong_letters) == 8:
    print("\nOh no! You have lost!")
    print(f"The word I was thinking of was {chosen_word}")
    return True
  else:
    return False

def win_check(dash,sentence,count):
  if dash not in sentence:
    print("Well done! You have won!")
    print(f"It took you only {count} guesses!")
    return True
  else:
    return False

def user_choice():
  while True:
    choice = input("\nWould you like to play again? (y/n): ")
    if choice.lower() == "y":
      tidy()
      print("\nYay! Let's play again!")
      guessed_letters.clear()
      wrong_letters.clear()
      print("Alright, I'm thinking of a new word... Okay I've got one!\n")
      break
    elif choice.lower() == "n":
      print("\nThanks for playing! See you next time!")
      exit()
    else:
      print("That is not a valid input. Try Again!")

def tidy():
  while True:
    tidy_choice = input("Would you like to tidy up the screen? (y/n): ")
    if tidy_choice.lower() == "y":
      print("\nOkay I will clear your screen for a new game!")
      time.sleep(2)
      clear()
      break
    elif tidy_choice.lower() == "n":
      print("\nOkay, I won't clear your screen for a new game!")
      break
    else:
      print("\nOops! That is not a valid input. Try again!")

if __name__ == "__main__":
  guessed_letters = []
  wrong_letters = []
  guess_count = 0
  welcome_message()
  main()