"""Problem statment :- Tony and Steve want to play a simple Board game. Write a code that has two personalities
implemented as Threads. They both will start from 0 and will finish at 100. Print the two lists
in the output, in which each list should contain the value of each dice occurrence and print the
Player who won. (Python)
Rules:
Each Player can start only if he gets 6 in dice occurrence.
One who reaches to 100 first is the winner. Output:
Player 1 Dice: [6, 3, 6, 1, ...]
Player 2 Dice: [6, 3, 2, 5, 1, 6, ...]
Player 1 Won"""
import random
l1,l2=[6],[6]
flag1,flag2=0,0
sum1,sum2,win=0,0,0,
player1,player2=0,0
while(win==0):
    n=0
    if(flag1==0):
        n=random.randint(1,6)
        if(n==6):
            flag1=1
    n = 0
    if (flag2 == 0):
        n = random.randint(1, 6)
        if (n == 6):
            flag2 = 1
    n=0
    if(flag1==1 and sum1<=100):
        n=random.randint(1,6)
        l1.append(n)
        sum1+=n
        if(sum1>=100):
            win=1
            player1 = 1
    if (flag2 == 1 and sum2 <= 100):
        n = random.randint(1, 6)
        l2.append(n)
        sum2 += n
        if (sum2 >= 100):
            win=1
            player2 = 1
print("Player 1 dice: ",l1)
print("Player 2 dice: ",l2)
if(player1==1):
    print("Player 1 won")
else:
    print("Player 2 won")