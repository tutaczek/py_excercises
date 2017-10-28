def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

print('Podaj liczbę:')
try:
    number = int(input())
except ValueError:
    print('To nie jest liczba. Skup się i podaj liczbę całkowitą:')
    number = int(input())

while True:
    number = collatz(number)
    print(number)
    if number == 1:
        break
    
