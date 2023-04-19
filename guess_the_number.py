import random

input_range = input('Type a number: ')

if input_range.isdigit():
    input_range = int(input_range)
    if input_range <= 0:
        print('Please enter a number greater than 0')
        quit()
else:
    print('Please enter a number')
    quit()

random_num = random.randint(0, input_range)

guesses = 0
while True:
    guesses += 1
    user_guess = input('Enter your guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('Please enter a number')
        continue

    if user_guess == random_num:
        print('You got it!')
        break
    elif user_guess < random_num:
        print('You are below the number')
    else:
        print('You are above the number')

print('You got it in', guesses, 'guesses')
