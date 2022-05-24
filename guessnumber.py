import random

#human guessing the number
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        print(guess)
        if guess > random_number:
            print('Your guess is too high')
        elif guess < random_number:
            print('Your guess is too low')
    print(f'Congrats you got the number {random_number}')

#computer guessing the number
def compguess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'The computer guessed the number {guess} correctly')
compguess(67492)