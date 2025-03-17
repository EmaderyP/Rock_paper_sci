import random

def Game():
    user = (input("what's your choice? 'r' for rock, 'p' for paper and 's' for scisors \n"))
    computer = random.choice(['r','p','s'])
    # print("computer choice is: " + computer)

    if user == computer:
        return 'its a tie!'
    
    if is_winner(user, computer):
        return 'you won!'
    
    return 'you lost!'

def is_winner(user, computer):
    # r>p , p > r , r > s 
    if (user == 'r' and computer == 'p') or (user == 'p' and computer == 'r') or (user == 'r' and computer == 's'):
        return True

print(Game())