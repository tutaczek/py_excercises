while True:
    print('Podaj swój wiek:')
    age = input()
    if age.isdecimal():
        break
    print('Wiek musi być wartością liczbową.')


while True:
    print('Wbierz nowe hasło (tylko litery i cyfry).')
    password = input()
    if password.isalnum():
        break
    print('Hasło musi składać się z liter i/lub cyfr.')
    
