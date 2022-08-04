import random
import colorama
import ctypes
import os
from colorama import *
from random import choice

colorama.init()


def ex():
    ans = input(Fore.RED + 'Уверен? y/n: ')
    if ans == 'y':
        os.abort()
    else:
        main()


def main():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW('Password generator by nickoff & ebankoff')
    print(Fore.YELLOW + Style.BRIGHT + 'Password generator by nickoff & ebankoff\n')

    lib = '1234567890_qwertyuiopasdfghjklzxcvbnm'

    try:
        ans1 = int(input(Fore.BLUE + 'Длина пароля: '))
        ans2 = int(input(Fore.BLUE + 'Сколько паролей делаем: '))
        print(Fore.YELLOW + Style.BRIGHT + '\nСТАРТУЕМ\n')
        for i in range(ans2):
            pas = ''
            for j in range(ans1):
                pas += random.choice(lib)
            with open('passwords.txt', 'a', encoding='utf8') as file:
                file.write(f'[{str(i)}] {pas}\n')
            print(Fore.BLUE + f'[{str(i)}]' + Fore.WHITE + ' | ' + Fore.GREEN + f'{pas}')
        print(Fore.YELLOW + Style.BRIGHT + '\nГотово')
        ans0 = input(Fore.BLUE + 'Выход? y/n: ')
        if ans0 == 'y':
            ex()
        else:
            main()
    except:
        print(Fore.RED + 'Произошла какая-то хуйня, попробуй ещё разик')


if __name__ == "__main__":
    main()