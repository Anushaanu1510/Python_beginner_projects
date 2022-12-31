import random


def play():
    user = input("What is your choice? 'r' for rock ,'p' for paper, 's' for scissors:")
    computer = random.choice(['r', 'p', 's'])

    print("Your choice is:",user)
    print("Computer's choice is",computer)

    if user == computer:
        return 'It\'s a tie'

    elif is_win(user, computer):
        return 'You Win'
    
    else:
        return 'You Lost'
    

def is_win(player, opponent):
    if (player == 'r' and opponent == 'p') or (player == 'p' and opponent == 's') or (player == 's' and opponent == 'r'):
        return True


print(play())