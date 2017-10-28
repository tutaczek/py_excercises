#! usr/bin/python3
#pw.py - Niebezpieczny program menedżera haseł

PASSWORDS = {'email': '12345',
             'blog': 'cosie2',
             'bagaż': '2468'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Użycie: python pw.py [konto] - skopiowanie hasła wskazanego konta')
    sys.exit()

account = sys.argv[1] #pierwszym argumentem wiersza poleceń jest nazwa konta.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Hasło do konta ' + account + ' zostało skopiowane do schowka.')
else:
    print('Nie istnieje konto o nazwie ' + account + ' .')
    
