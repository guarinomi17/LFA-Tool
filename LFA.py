import re

# create english language dictionary
# https://github.com/dwyl/english-words
english_dictionary_raw = open("dictionary.txt")
english_dictionary = english_dictionary_raw.read().split()
english_dictionary_raw.close()

# creating values, dictionaries, lists, variables that are needed
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
encrypted = ''
real = ''
encrypted_to_be_replaced = ''
ciphertext = input("Enter the encrypted text: \n")
ciphertext = ciphertext.upper()
ciphertext_new = ciphertext
chars = ''
ciphertext_alpha = re.compile('[^a-zA-Z^]').sub('', ciphertext)
unique_chars = len(set(ciphertext_alpha)) - 1
real_used = ['']
encrypted_used = ['']
user_input = ''
letter_dict = {}
already_used = {}
english_frequencies = {'E': .1202, 'T': .0910, 'A': .0812, 'O': .0768, 'I': .0731, 'N': .0695, 'S': .0628, 'R': .0602, 'H': .0592, 'D': .0432, 'L': .0398, 'U': .0288, 'C': .0271, 'M': .0261, 'F': .0230, 'Y': .0211, 'W': .0209, 'G': .0203, 'P': .0182, 'B': .0149, 'V': .0111, 'K': .0069, 'X': .0017, 'Q': .0011, 'J': .0010, 'Z': .0007}
english_frequencies_adjusted = {}
cipher_length = len(ciphertext_alpha)


# ----------------------------------------------------------------------------------------
# creates a dictionary listing the estimated occurrences of each letter based on the length of the ciphertext
def create_avg_dict():
    # adds each letter to the dictionary, multiplies the frequency by the length of the cipher to estimate occurrences
    for letter, frequency in english_frequencies.items():
        adjusted_frequency = cipher_length * frequency
        english_frequencies_adjusted[letter] = int(round(adjusted_frequency))
    return english_frequencies_adjusted


# replace function: the following functions are used for substituting letters
def get_replacements():
    # function gets input from user
    global encrypted
    global real
    # repeats loop until the ciphertext letter is valid
    while encrypted in encrypted_used or len(encrypted) > 1 or encrypted.isnumeric():
        encrypted = input("Enter an ciphertext letter to be substituted: \n").upper()
        if encrypted in encrypted_used:
            print('\033[91mEnter a letter that has not already been replaced. \033[99m\n')
        if len(encrypted) > 1:
            print('\033[91mEnter a single letter. \033[99m\n')
        if encrypted.isnumeric():
            print('\033[91mYou can not substitute a number. \033[99m\n')
    # repeats loops until the plaintext letter is valid
    while real in real_used or len(real) > 1 or real.isnumeric():
        real = input("Enter a plaintext letter to substitute " + encrypted + ' with: \n').lower()
        if real in real_used:
            print('\033[91mEnter a substitute letter that has not already been used. \033[99m\n')
        if len(real) > 1:
            print('\033[91mEnter a single letter. \033[99m\n')
        if real.isnumeric():
            print('\033[91mYou can not replace a number. \033[99m\n')


def replace_letter():
    # replaces the desired characters in the ciphertext
    global ciphertext_new
    ciphertext_new = ciphertext_new.replace(encrypted, real)
    # adds the characters to the dictionary/lists for later use
    already_used.update({real: encrypted})
    real_used.append(real)
    encrypted_used.append(encrypted)

def replace_function():
    # gets the user input for substitution, then substitutes the letters and prints a message. (also changes the 'real' and 'encrypted' variables back to blank.)
    # I realize as I'm writing this comment that i didn't need to use global variables and reset them at the end of the function, but it is too late to change. (the same applies for a few of the functions)
    global real
    global encrypted
    get_replacements()
    replace_letter()
    print("Replaced " + encrypted + ' with ' + real + '\n')
    real = ''
    encrypted = ''
    main()

# dictionary
def update_dictionary():
    # updates the ciphertext frequency dictionary for the remaining letters
    letter_dict = {}
    for letter in ciphertext_new:
        if letter.isupper():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    sorted_dict = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict

# color text
def color_ciphertext(ciphertext_colored):
    # colors capital(ciphertext) letters red for a clearer visualization
    for letter in ciphertext_colored:
        if letter.isupper():
            ciphertext_colored = ciphertext_colored.replace(letter, '\033[91m' + letter + "\033[99m")
    return ciphertext_colored

# print current ciphertext
def current_cipher_message():
    # updates the dictionaries, then prints the current ciphertext and frequencies
    average_dict = create_avg_dict()
    sorted_dict = update_dictionary()
    print('The frequencies of the current encrypted letters are ' + str(sorted_dict) + '\n')
    print('The average frequencies of the letters in a string of this length are ' + str(average_dict) + '\n')
    ciphertext_colored = ciphertext_new
    ciphertext_colored = color_ciphertext(ciphertext_colored)
    print('The current ciphertext is "' + ciphertext_colored + '"\n')
    # (only shows this list if at least one letter has already been substituted)
    if len(already_used) != 0:
        print('The already decrypted letters are: (plaintext:ciphertext): ' + str(already_used) + '\n')



# undo function
def undo():
    # The inverse of the replace function
    # takes a plaintext letter, finds it in the dictionary of previous substitutions, and reverts the change + updates the dictionaries
    global ciphertext_new
    undoInput = ''
    while len(undoInput) != 1:
        undoInput = input("Enter a plaintext letter to return to ciphertext \n")
    for key, value in already_used.items():
        if key == undoInput:
            undoPlaintext = key
            undoCiphertext = value
    del already_used[key]
    real_used.remove(undoPlaintext)
    encrypted_used.remove(undoCiphertext)
    ciphertext_new = ciphertext_new.replace(undoPlaintext, undoCiphertext)
    main()


# solver function
def solver():
    # splits the ciphertext into each individual word
    ciphertext_split = ciphertext_new.split(' ')
    index = 0
    string = ''
    # creates a string that shows the index value of each word
    for word in ciphertext_split:
        string = string + word + '(' + str(index) + ') '
        index += 1
    # prints the string
    print(string)
    # gets user input to decide which word to solve
    # repeats loop until the input is a valid index value
    word_index = 'a'
    while True:
        if word_index.isdigit() == 0:
            try:
                word_index = input('Enter the index value of the word you want to solve: \n')
            except ValueError:
                print('Enter a digit that corresponds to the desired word. ')
        elif int(word_index) > len(ciphertext_split):
            try:
                word_index = input('Enter the index value of the word you want to solve: \n')
            except IndexError:
                print('Enter a digit that corresponds to the desired word. ')
        else:
            break
    # uses the input to select the desired word from the ciphertext
    word_index = int(word_index)
    test_word = ciphertext_split[word_index]
    # makes a copy of the original test word before modifying it
    test_word_original = test_word
    # if string ends in punctuation, removes punctuation
    if test_word[-1].isalnum() == 0:
        test_word = test_word[:-1]
    # replaces ciphertext (uppercase) letters with question marks
    for letter in test_word:
        if letter.isupper():
            test_word = test_word.replace(letter, '?')
    # counts the amount of plaintext letters (the length of the word minus the number of ciphertext letters)
    non_blanks = len(test_word)-test_word.count('?')
    possible_words = []
    # checks the word against every word in the English dictionary.
    # first checks for matching word length, then checks for matching plaintext letters with the same index within the words
    # if every plaintext letter matches, the word is added to the list of possible matches
    for word in english_dictionary:
        letter_index = 0
        matches = 0
        if len(word) == len(test_word):
            for letter in test_word:
                if letter.lower() == word[letter_index].lower():
                    matches += 1
                letter_index += 1
            if matches == non_blanks:
                possible_words.append(word)
    # checks the possible words against the list of already substituted plaintext letters
    # if the letter in the ciphertext word isn't decrypted, it takes the dictionary word's letter in the same index position
    # if the dictionary word's letter is already in the list of used plaintext letters, the word is not a possibility, and is removes from the list
    if len(possible_words) > 0:
        for word in possible_words:
            current_index = 0
            possible = 1
            for letter in word:
                if letter != test_word[current_index] and possible != 0:
                    if letter not in real_used:
                        possible = 1
                    else:
                        possible = 0
                current_index += 1
            if possible == 0:
                possible_words.remove(word)
    # prints the list
    print('The possiblities of ' + test_word_original + ' are ' + str(possible_words).lower() + '\n')
    # returns to the main loop
    main()

# --------------------------------------------------------------------------------------


def main():
    # updates dictionaries and prints the ciphertext
    update_dictionary()
    current_cipher_message()
    # list of valid user inputs
    valid_responses = ['r', 'replace', 'u', 'undo', 'h', 'help', 'solved', 'highlight', 'hl']
    user_input = ''
    # repeats loop until user enters a valid response
    # once a valid response is entered, the corresponding function is ran
    while user_input not in valid_responses:
        user_input = str(input("What would you like to do, replace(r), undo(u), help(h), or highlight(hl)? \n"))
        if user_input == 'replace' or user_input == 'r':
            replace_function()
        if user_input == 'undo' or user_input == 'u':
            undo()
        if user_input == 'help' or user_input == 'h':
            solver()
        # if input is invalid, prints a red message
        if user_input not in valid_responses:
            print('\033[91mInvalid response\033[99m \n')
            main()
        if user_input == 'solved':
            print('The decrypted cipher is "' + ciphertext_new + '"')
        if user_input == 'highlight' or user_input == 'hl':
            # gets user input of letter to be highligted, and prints the ciphertext with the letter highlighted
            highlightletter = input("Enter a letter to be highlighted : (either capital or lowercase) \n")
            ciphertext_colored = color_ciphertext(ciphertext_new)
            for letter in ciphertext_colored:
                if letter == highlightletter:
                    ciphertext_colored = ciphertext_colored.replace(letter, '\033[94m' + letter)
            print('The ciphertext with ' + highlightletter + ' highlighted: "' + ciphertext_colored + '"\n')
            main()


# --------------------------------------------------------------------------------------
main()
