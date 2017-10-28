#! python3
#GuessTheNumber_v.2_PL.py - gierka po polsku

import random

print('Cześć! Zagdnij liczbę z przedziału 1 do 20!')

number = random.randint(0, 20)

while True:
    answer = int(input())
    if answer == number:
        print('Brawo! Udało Ci się :D Chcesz zagrać jeszcze raz? Wpisz T lub N')
        choice = input()
        if choice == 'T':
            print('Zgaduj jeszcze raz!')
            number = random.randint(0, 20)
            continue
        elif choice == 'N':
            break            
    elif answer < number:
        print('Za mała. Spróbuj jeszcze raz.')
    elif answer > number:
        print('Za duża. Spróbuj jeszcze raz.')
              
