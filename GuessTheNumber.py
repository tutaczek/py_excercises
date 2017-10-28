import random

print('Hey babe, guess the number and I am yours!')

number = random.randint(0, 20)

while True:
    answer = int(input())
    if answer == number:
        print('Congratulations, I am yours! :D')
        break
    elif answer < number:
        print('Too little, try again.')
    elif answer > number:
        print('Too big, try again.')
              
