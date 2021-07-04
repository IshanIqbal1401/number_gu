import random
from logo_no import logo
print(' Welcome to the Number Guessing Game!\n I\'m thinking of a number between 1 and 100.')
answer=random.randint(1,100)
game_finished=False
print(answer)
EASY=10
HARD=5
def set_difficulty():
    difficulty=input('Choose a difficulty. Type \'easy\' or \'hard\':')
    if difficulty=='easy':
        return EASY
    else:
        return HARD
def check_answer():
    print(logo)
    turns=set_difficulty()
    while turns>0:
        user_no_input=int(input('Make a guess : '))
        turns-=1
        if user_no_input>answer:
            print('The input is too high')
            print(f'U have {turns} left')
            continue
        if user_no_input<answer:
            print('The input is too low')
            print(f'U have {turns} chances left')
            continue
        if user_no_input==answer:
            print(f'The input is {answer}, U WIN!!')
            break
    print(f'U lose ,The correct answer is {answer}')

check_answer()
while not game_finished:
        feedback=input('Do u want to play again? ')
        if feedback=='yes':
            check_answer()
        else:
            game_finished=True

    
  



