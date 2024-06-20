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
        guess_count = 0
        while is_endgame == False:
            guess = user_guess()
            guess_count = guess_check(chosen_word, guess, guess_count)
            is_endgame = display(chosen_word, guessed_letters, guess_count)
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
    length = len(chosen_word)
    print(f"The word is {length} letters long\n")
    display(chosen_word, guessed_letters, guess_count=0)
    return chosen_word


def user_guess():
    while True:
        guess = input("\nPlease enter your guess:")
        if len(guess) == 1 and guess.isalpha():
            return guess.lower()
        else:
            print("That is not a valid input. Try Again!")


def guess_check(guess, count):
    if guess in word and guess not in guessed_letters:
        print(f"\nNice work! {guess.upper()} is in the word!\n")
        guessed_letters.append(guess)
        return count+1
    elif guess not in word and guess not in wrong_letters:
        print(f"\nOh no! There is no {guess.upper()} in this word!\n")
        wrong_letters.append(guess)
        drawing(len(wrong_letters), wrong_letters)
        return count+1
    else:
        print("\nYou already guessed that letter! Try again!")
        return count


def win_check(dash, sentence, count):
    if dash not in sentence:
        print("Well done! You have won!")
        print(f"It took you only {count} guesses!")
        return True
    else:
        return False


def lose_check():
    if len(wrong_letters) == 8:
        print("\nOh no! You have lost!")
        print(f"The word I was thinking of was {chosen_word}")
        return True
    else:
        return False


def display(chosen_word, guessed_letters, guess_count):
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
        is_solved = win_check(dash, sentence, guess_count)
        is_lost = lose_check()
    if is_solved or is_lost:
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
    pass


if __name__ == "__main__":
    guessed_letters = []
    wrong_letters = []
    sentence = []
    welcome_message()
    main()
