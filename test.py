import re
import random
from colorama import init
init(autoreset=True)
regex = re.compile('[^a-zA-Z^]')


#create english language dictionary
english_dictionary_lengths = {}
english_dictionary_raw = open("dictionary.txt")
english_dictionary = english_dictionary_raw.read().split()
english_dictionary_raw.close()

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
encrypted = ''
real = ''
encrypted_to_be_replaced = ''
ciphertext = input("Enter the encrypted text")
ciphertext = ciphertext.upper()
ciphertext_new = ciphertext
chars = ''
ciphertext_alpha = regex.sub('', ciphertext)
unique_chars = len(set(ciphertext_alpha)) -1
real_used = ['']
encrypted_used = ['']
user_input = ''
letter_dict = {}
already_used = {}
#----------------------------------------------------------------------------------------
#replace function
def get_replacements():
    global encrypted
    global real
    while encrypted in encrypted_used:
        encrypted = input("Enter an encrypted letter to be replaced:").upper()
        if encrypted in encrypted_used:
            print('Enter a letter that has not already been replaced.')
    while real in real_used:
        real = input("Enter a real letter to replace " + encrypted + ' with:').lower()
        if real in real_used:
            print('Enter a replacement letter that has not already been used.')
def replace_letter():
    global ciphertext_new
    ciphertext_new = ciphertext_new.replace(encrypted, real)
    already_used.update({real: encrypted})
    real_used.append(real)
    encrypted_used.append(encrypted)
def update_dictionary():
    letter_dict = {}
    for letter in ciphertext_new:
        if letter.isupper():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    global updated_dict
    global sorted_updated_dict
    global sorted_dict
    updated_dict = {key: value for key, value in letter_dict.items()
                 if value is not 0}
    sorted_updated_dict = sorted(updated_dict.items(),key=lambda x: x[-1], reverse=True)
    sorted_dict = sorted(letter_dict.items(),key=lambda x: x[-1], reverse=True)
def current_cipher_message():
    print('The frequencies of the current encrypted letters are ' + str(sorted_dict))
    print('The updated cipher is ' + ciphertext_new)
    print('The already decrypted letters are: (plaintext:ciphertext): ' + str(already_used))
def replace_function():
    global real
    global encrypted
    get_replacements()
    replace_letter()
    update_dictionary()
    print("Replaced " + encrypted + ' with ' + real + '\n')
    current_cipher_message()
    real = ''
    encrypted = ''

#undo function
def undo():
    global ciphertext_new
    undoInput = ''
    while len(undoInput) != 1:
        undoInput = input("Enter a plaintext letter to return to ciphertext")
    for key, value in already_used.items():
        if key == undoInput:
            undoPlaintext = key
            undoCiphertext = value
    del already_used[key]
    real_used.remove(undoPlaintext)
    encrypted_used.remove(undoCiphertext)
    ciphertext_new = ciphertext_new.replace(undoPlaintext, undoCiphertext)
    update_dictionary()
    current_cipher_message()

#solver function
def solver():
    word_index = int(input('Please enter the index value of the word you want to solve: '))
    ciphertext_split = ciphertext_new.split(' ')
    testWord = ciphertext_split[word_index]
    for letter in testWord:
        if letter.isupper():
            testWord = testWord.replace(letter, '?')
    nonBlanks = len(testWord)-testWord.count('?')
    for word in english_dictionary:
        incLetter = 0
        incMatch = 0
        if len(word) == len(testWord):
            for letter in testWord:
                if letter == word[incLetter]:
                    incMatch += 1
                incLetter += 1
            if incMatch == nonBlanks:
                print(word)

#--------------------------------------------------------------------------------------
def input_decision():
    global user_input
    while user_input == '' or user_input == 'replace' or user_input == 'undo' or user_input == 'help':
        if user_input == '':
            user_input = str(input("What would you like to do, replace(r), undo(u), or get possible words(h)? (type solved if the message is fully decrypted):"))
        if user_input == 'replace':
            replace_function()
            user_input = ''
        if user_input == 'undo':
            undo()
            user_input = ''
        if user_input == 'h':
            solver()
            user_input = ''

#--------------------------------------------------------------------------------------
update_dictionary()
current_cipher_message()

input_decision()
