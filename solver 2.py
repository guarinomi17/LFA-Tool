ciphertext_new = 'aPPle'

english_dictionary_lengths = {}
english_dictionary_raw = open("dictionary.txt")
english_dictionary = english_dictionary_raw.readlines()
for line in english_dictionary:
    english_word_len = len(line) - 1
    english_dictionary_lengths.update({line: english_word_len})

english_dictionary_lengths = {'apple':5, 'aisle':5, 'agile':5, 'abase': 5}

def solver():
    ciphertext_split = ciphertext_new.split()
    word_check = input("What word would you like to solve?")
    testing_word = ciphertext_split[word_check]
    for char in testing_word:
        if char.isupper() == 1:
            testing_word = testing_word.replace(char, ' ')
    print(testing_word)
    print(len(testing_word))
    for key, value in english_dictionary_lengths.items():
        if len(testing_word) == value:
            print(key)
            current_index = 0
            success = 0
            while current_index < value:
                if testing_word[current_index] == key[current_index]:
                    print(testing_word[current_index] + ' is equal to ' + key[current_index])
                    if int(current_index) == len(testing_word) - 1:
                        current_index += 1
                    success += 1
                elif testing_word[current_index] == ' ':
                    if int(current_index) == len(testing_word) - 1:
                        current_index += 1
                    success += 1
                else:
                    current_index += 1
            if current_index == success:
                print(key)
solver()
