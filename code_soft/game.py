import random
c="yes"
while(c=='yes'):
    Options = ('rock','paper','scissor')
    computer = random.choice(Options)
    Player = None
    while Player not in Options:
        Player = input('Enter One Option from (Rock,Paper,Scissor) = ')
        if computer == Player:
            print("Tie")
        elif computer == 'rock' and Player == 'paper':
            print("YOU WIN")
        elif computer == 'paper' and Player == 'scissor':
            print("YOU WIN")
        elif computer == 'scissor' and Player == 'rock':
            print("YOU WIN")
        else:
            print("COMPUTER WINS")
    c=input('Enter "yes" to continue = ')