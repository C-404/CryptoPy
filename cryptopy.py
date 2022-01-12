import cryptocode
from colorama import Fore, Style
print('╭━━━╮╱╱╱╱╱╱╱╱╭╮╱╱╱╭━━━╮\n┃╭━╮┃╱╱╱╱╱╱╱╭╯╰╮╱╱┃╭━╮┃\n┃┃╱╰╋━┳╮╱╭┳━┻╮╭╋━━┫╰━╯┣╮╱╭╮\n┃┃╱╭┫╭┫┃╱┃┃╭╮┃┃┃╭╮┃╭━━┫┃╱┃┃\n┃╰━╯┃┃┃╰━╯┃╰╯┃╰┫╰╯┃┃╱╱┃╰━╯┃\n╰━━━┻╯╰━╮╭┫╭━┻━┻━━┻╯╱╱╰━╮╭╯\n╱╱╱╱╱╱╭━╯┃┃┃╱╱╱╱╱╱╱╱╱╱╭━╯┃\n╱╱╱╱╱╱╰━━╯╰╯╱╱╱╱╱╱╱╱╱╱╰━━╯\n'+Fore.LIGHTRED_EX+'by c404')
while True:
    mode = input(Fore.LIGHTMAGENTA_EX+'Select mode: 1 for encode, 2 for decode, exit for exit\n'+Fore.LIGHTMAGENTA_EX+'>>'+Fore.LIGHTCYAN_EX+'')

    if mode == '1':
        key = input(Fore.LIGHTMAGENTA_EX+'Input your key for encoding and decoding:\n>>'+Fore.LIGHTCYAN_EX+'')
        print(Fore.LIGHTMAGENTA_EX+'Input text for encode:')
        text = input(Fore.LIGHTMAGENTA_EX+'>>'+Fore.LIGHTCYAN_EX)
        encoded = cryptocode.encrypt(text, key)
        print('encoded:\n', Fore.LIGHTMAGENTA_EX+encoded)
        Style.RESET_ALL
        decoded = cryptocode.decrypt(encoded, key)
        print(Fore.LIGHTCYAN_EX+'decoded:\n', Fore.LIGHTMAGENTA_EX+decoded)
    
    elif mode == '2':
        key = input(Fore.LIGHTCYAN_EX+'Input your key for decoding:\n>>')
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