import re
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style
regex = re.compile('[^a-zA-Z^]')

encrypted = ''
real = ''
encrypted_to_be_replaced = ''
ciphertext = input("Enter the encrypted text")
ciphertext = Fore.RED + ciphertext.upper()
ciphertext_new = ciphertext
chars = ''
ciphertext_alpha = regex.sub('', ciphertext)
unique_chars = len(set(ciphertext_alpha)) -1
real_used = ['']
encrypted_used = ['']
#init letter counts
a_count = 0
b_count = 0
c_count = 0
d_count = 0
e_count = 0
f_count = 0
g_count = 0
h_count = 0
i_count = 0
j_count = 0
k_count = 0
l_count = 0
m_count = 0
n_count = 0
o_count = 0
p_count = 0
q_count = 0
r_count = 0
s_count = 0
t_count = 0
u_count = 0
v_count = 0
w_count = 0
x_count = 0
y_count = 0
z_count = 0

def get_replacements():
    global encrypted
    global real
    while encrypted in encrypted_used:
        encrypted = input("Enter an encrypted letter to be replaced:").upper()
        if encrypted in encrypted_used:
            print(Fore.RED + 'Enter a letter that has not already been replaced.')
    while real in real_used:
        real = input("Enter a real letter to replace " + encrypted + ' with:').lower()
        if real in real_used:
            print(Fore.RED + 'Enter a replacement letter that has not already been used.')
def replace_letter():
    global ciphertext_new
    ciphertext_new = ciphertext_new.replace(encrypted, real)
    real_used.append(real)
    encrypted_used.append(encrypted)
def updated_cipher():
    global ciphertext_new
    print()
    print("Replaced " + encrypted + ' with ' + real)
    print()
    print('The frequencies of the remaining letters are ' + str(sorted_updated_dict))
    print(Fore.MAGENTA + 'The updated cipher is ' + ciphertext_new)
    print()
    print('The encrypted letters ' + str(encrypted_used) + ', and the real letters ' + str(real_used) + ' have already been changed.')
def function():
    get_replacements()
    replace_letter()
    count_letters()
    update_dictionaries()
    updated_cipher()

def count_letters():
    global a_count
    global b_count
    global c_count
    global d_count
    global e_count
    global f_count
    global g_count
    global h_count
    global i_count
    global j_count
    global k_count
    global l_count
    global m_count
    global n_count
    global o_count
    global p_count
    global q_count
    global r_count
    global s_count
    global t_count
    global u_count
    global v_count
    global w_count
    global x_count
    global y_count
    global z_count
    a_count = int(ciphertext_new.count("A"))
    b_count = int(ciphertext_new.count("B"))
    c_count = int(ciphertext_new.count("C"))
    d_count = int(ciphertext_new.count("D"))
    e_count = int(ciphertext_new.count("E"))
    f_count = int(ciphertext_new.count("F"))
    g_count = int(ciphertext_new.count("G"))
    h_count = int(ciphertext_new.count("H"))
    i_count = int(ciphertext_new.count("I"))
    j_count = int(ciphertext_new.count("J"))
    k_count = int(ciphertext_new.count("K"))
    l_count = int(ciphertext_new.count("L"))
    m_count = int(ciphertext_new.count("M"))
    n_count = int(ciphertext_new.count("N"))
    o_count = int(ciphertext_new.count("O"))
    p_count = int(ciphertext_new.count("P"))
    q_count = int(ciphertext_new.count("Q"))
    r_count = int(ciphertext_new.count("R"))
    s_count = int(ciphertext_new.count("S"))
    t_count = int(ciphertext_new.count("T"))
    u_count = int(ciphertext_new.count("U"))
    v_count = int(ciphertext_new.count("V"))
    w_count = int(ciphertext_new.count("W"))
    x_count = int(ciphertext_new.count("X"))
    y_count = int(ciphertext_new.count("Y"))
    z_count = int(ciphertext_new.count("Z"))

def update_dictionaries():
    global updated_dict
    global sorted_updated_dict
    global sorted_dict
    updated_dict = {key: value for key, value in letter_dict.items()
                 if value is not 0}
    sorted_updated_dict = sorted(updated_dict.items(),key=lambda x: x[-1], reverse=True)
    sorted_dict = sorted(letter_dict.items(),key=lambda x: x[-1], reverse=True)

def create_dict():
    global letter_dict
    letter_dict = {
    "a": a_count,
    "b": b_count,
    "c": c_count,
    "d": d_count,
    "e": e_count,
    "f": f_count,
    "g": g_count,
    "h": h_count,
    "i": i_count,
    "j": j_count,
    "k": k_count,
    "l": l_count,
    "m": m_count,
    "n": n_count,
    "o": o_count,
    "p": p_count,
    "q": q_count,
    "r": r_count,
    "s": s_count,
    "t": t_count,
    "u": u_count,
    "v": v_count,
    "w": w_count,
    "x": x_count,
    "y": y_count,
    "z": z_count,
}

count_letters()

#dictionary
letter_dict = {
    "a": a_count,
    "b": b_count,
    "c": c_count,
    "d": d_count,
    "e": e_count,
    "f": f_count,
    "g": g_count,
    "h": h_count,
    "i": i_count,
    "j": j_count,
    "k": k_count,
    "l": l_count,
    "m": m_count,
    "n": n_count,
    "o": o_count,
    "p": p_count,
    "q": q_count,
    "r": r_count,
    "s": s_count,
    "t": t_count,
    "u": u_count,
    "v": v_count,
    "w": w_count,
    "x": x_count,
    "y": y_count,
    "z": z_count,
}
updated_dict = {key: value for key, value in letter_dict.items()
             if value is not 0}
sorted_updated_dict = sorted(updated_dict.items(),key=lambda x: x[-1], reverse=True)
sorted_dict =sorted(letter_dict.items(),key=lambda x: x[-1], reverse=True)

remaining_letters_message = 'The frequencies of the remaining letters in the cipher are '
#    print(updated_message, sorted_dict)
#    print()
#    print(Fore.MAGENTA + 'The current cipher is ' +ciphertext_new)
print()
print('The encrypted message is ' + ciphertext_new)
print('The frequencies of the letters in the cipher are ' + str(sorted_dict))
print()

while unique_chars > 0:
    print('There are ' + str(unique_chars) + ' letters to be replaced')
    function()
    unique_chars -= 1
