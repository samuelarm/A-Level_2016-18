""" Hangman Game (v1.0)
    Name: Mr Gorman
    Date: 22/09/2016
    """

import os
import random

def load_file(filename):
    """ Function to return a word list from a plain text file;
        Note: You will need to open the file, read and append
        each line to an array (or list), close the file and
        then return the array.
        """
    word_list = []

    with open(filename, "r") as file:
        for line in file:
            line = line.replace("\n", "").upper()
            word_list.append(line)

    return word_list

def select_word(word_list):
    """ Function to return a random word from an array of words;
        Note: You will need to import the random module and use
        random.randint() to select a random index in the array.
        """
    index = random.randint(0, len(word_list) - 1)
    word = word_list[index]
    return word

def find_character(char, word):
    """ Function to return the indices of a character in word;
        Note: This should return a list of indices or an empty list
        if the character is not found.
        """
    char_indices = []
    index = 0
    for character in word:
        if character == char:
            char_indices.append(index)
        index += 1

    return char_indices

##def find_char_r(char, word, index=-1): 
##    """ Function to recursively return the indices of character in word: 
##        Note: This should return an array of indices containing: 
##        1 index if the character appears only once, multiple indices if  
##        the character appears more than once and an empty array if the 
##        character is not found. 
##        """  
##    index = word.find(char, index + 1) 
##    if index == -1: 
##        return [] 
##    return [index] + find_char_r(char, word, index) 

def create_placeholders(word):
    """ Function to return a list of placeholders corresponding to 
        the length of the word, adjusted for spaces; also returns 
        the number of spaces.
        """
    placeholders = ["_" for i in range(len(word))]
    spaces = find_character(" ", word)
    n_spaces = len(spaces)

    if n_spaces > 0:
        for index in spaces:
            placeholders[index] = " "
    
    return placeholders, n_spaces

def display_info(placeholders, letters_remaining, attempts_remaining):
    """ Procedure for printing current placeholders and stats to the screen
        """
    print()
    for place in placeholders:
        print(place, end=" ")
    print("\n\nLetters remaining = %d, Attempts remaining = %d\n" % (letters_remaining, attempts_remaining))

def main():
    """ Note: This is your main function and should contain your game loop.
        """
    VALID_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    filename = os.path.dirname(__file__) + "\word_list.txt" # os.path.dirname() required if running outside of the script directory
    word_list = load_file(filename)
    game_over = False

    while not game_over:

        word = select_word(word_list)
        placeholders, n_spaces = create_placeholders(word)
        n_chars = len(word)
        letters_remaining = n_chars - n_spaces
        attempts_remaining = 10
        letters_guessed = []
        turn_over = False

        while not turn_over:

            display_info(placeholders, letters_remaining, attempts_remaining)

            valid_input = False
            while not valid_input:        
                char = input("Enter a letter: ").upper()
                if len(char) == 1 and VALID_CHARS.find(char) != -1:
                    valid_input = True
                else:
                    print("Invalid input!")

            char_indices = find_character(char, word)
            n_chars_found = len(char_indices)

            if letters_guessed.count(char) == 0:
                if n_chars_found > 0:
                    for index in char_indices:
                        placeholders[index] = char
                    letters_guessed.append(char)
                    letters_remaining -= n_chars_found
                    print("That's right!")
                else:
                    letters_guessed.append(char)
                    attempts_remaining -= 1
                    print("That's wrong!")
            else:
                print("You already guessed that letter!")
            
            if attempts_remaining == 0:
                print("YOU LOSE!")
                turn_over = True
            elif letters_remaining == 0:
                print("YOU WIN!")
                turn_over = True

        print("The word was: %s" % word)
        
        valid_input = False
        while not valid_input:
            player_input = input("\nDo you want to play again (y/n)? ").lower()
            if player_input == "y":
                valid_input = True
            elif player_input == "n":
                valid_input = True
                game_over = True

if __name__ == "__main__":
    main()
    
