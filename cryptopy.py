import cryptocode
import random
from colorama import Fore, Style
print(Fore.LIGHTGREEN_EX+' _____                  _       ______      ')
print('/  __ \                | |      | ___ \     ')
print('| /  \/_ __ _   _ _ __ | |_ ___ | |_/ /   _ ')
print("| |   | '__| | | | '_ \| __/ _ \|  __/ | | |")
print('| \__/\ |  | |_| | |_) | || (_) | |  | |_| |')
print('\____/_|   \__, |  .__/\__\\___/ |_|  \__, |')
print('             __/ | |                   __/ |')
print('            |___/|_|                  |___/ ')
print(Fore.LIGHTGREEN_EX+'by c404')
while True:
    mode = input(Fore.LIGHTMAGENTA_EX+'Select mode: 1 for encode, 2 for decode, exit for exit\n\b'+Fore.LIGHTMAGENTA_EX+'>>'+Fore.LIGHTCYAN_EX+'')

    if mode == '1':
        key = input(Fore.LIGHTMAGENTA_EX+'Input your key for encoding and decoding\nfor generate random key input r\n>>'+Fore.LIGHTCYAN_EX+'')
        if key == 'r':
            chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"*:;()/?!$~`|•√π÷×¶∆£¢€¥^°={}\%©®™✓][    '
            length = int(input('length key?'+ "\n"))
            for n in range(100):
                key =''
            for i in range(length):
                key += random.choice(chars)
            print(key)
        else:
                pass
        print(Fore.LIGHTMAGENTA_EX+'Input text for encode:')
        text = input(Fore.LIGHTMAGENTA_EX+'>>'+Fore.LIGHTCYAN_EX)
        encoded = cryptocode.encrypt(text, key)
        print('encoded:\n', Fore.LIGHTMAGENTA_EX+encoded)
        Style.RESET_ALL
        decoded = cryptocode.decrypt(encoded, key)
        print(Fore.LIGHTCYAN_EX+'decoded:\n', Fore.LIGHTMAGENTA_EX+decoded)
    
    elif mode == '2':
        key = input(Fore.LIGHTMAGENTA_EX+'Input your key for decoding:\n>>'+Fore.LIGHTCYAN_EX+'')
        text = input(Fore.LIGHTMAGENTA_EX+'Input encoded text:\n>>'+Fore.LIGHTCYAN_EX+'')
        decoded = cryptocode.decrypt(text, key)
        if decoded == False:
            print('Invalid encoded text')
        else:
            print(Fore.LIGHTMAGENTA_EX+'Your text:', decoded)

    elif mode == 'exit':
        quit()
    else:
        print(Fore.RED+'[•]Unknown command')