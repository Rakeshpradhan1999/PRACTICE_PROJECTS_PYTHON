import random

user_win = 0
computer_win = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_choose = options[random_number]

    print('Computer picked', computer_choose)

    if user_input == 'rock' and computer_choose == 'scissors':
        print('You win!')
        user_win += 1
    elif user_input == 'paper' and computer_choose == 'rock':
        print('You win!')
        user_win += 1
    elif user_input == 'scissor' and computer_choose == 'paper':
        print('You win!')
        user_win += 1
    else:
        print('You lost!')
        computer_win += 1

if user_win != 0 or computer_win != 0:
    print('You won', user_win, 'times!')
    print('You lost', computer_win, 'times!')

print('Goodbye!')
