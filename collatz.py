def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

print('Podaj liczbę:')
number = int(input())

while True:
    number = collatz(number)
    print(number)
    if number == 1:
        break
    
