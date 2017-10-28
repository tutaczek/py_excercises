birthdays = {'Alicja': '1 kwietnia', 'Bob': '12 grudnia', 'Karol': '4 marca'}

while True:
    print('Podaj imię: (pozostaw puste, aby zakończyć program.')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' to dzień urodzin osoby imieniem ' + name + '.')
    else:
        print('Nie zanleziono informacji o urodzinach osoby imieniem ' + name + '.')
        print('Kiedy przypadają te urodziny?')
        bday = input()
        birthdays[name] = bday
        print('Baza danych urodzin została zaktualizowana')
              
