from random import choice
from hangman_art import drawing


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
    pass


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
    if guess in chosen_word and guess not in guessed_letters:
        print(f"\nNice work! {guess.upper()} is in the word!\n")
        guessed_letters.append(guess)
        return count+1
    elif guess not in chosen_word and guess not in wrong_letters:
        print(f"\nOh no! There is no {guess.upper()} in this word!\n")
        wrong_letters.append(guess)
        hangman(wrong_letters)
        return count+1
    else:
        print("\nYou already guessed that letter! Try again!")
        return count


def win_check(dash, sentence, count):
    pass


def hangman(wrong_letters):
    pass


def lose_check():
    pass


def display(chosen_word, guessed_letters, guess_count):
    dash = "___ "
    sentence = []
    for letter in chosen_word:
        if letter in guessed_letters:
            sentence.append(letter)
            sentence.append(" ")
        else:
            sentence.append(dash)
    print("\n")
    print("".join(sentence))
    return win_check(dash, sentence, guess_count)


def user_choice():
    pass


if __name__ == "__main__":
    guessed_letters = []
    wrong_letters = []
    sentence = []
    welcome_message()
    main()
