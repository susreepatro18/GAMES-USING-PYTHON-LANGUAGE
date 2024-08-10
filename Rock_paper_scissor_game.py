import random
user_wins=0
computer_wins=0
options =["rock","paper","scissors"]
options[0]
while True:
    user_input=input("type ROCK/PAPER/SCISSORS or Q to quit").lower()
    if user_input.lower()=="q":
        break

    if user_input not in options:
        continue
    random_number =random.randint(0,2)
    computer_pick=options[random_number]
    print("computer picked :",computer_pick)
    if user_input =="rock" and computer_pick=="scissors":
        print("youu wonnnn!!!!!!hurrayyyy")
        user_wins=user_wins+1
    elif user_input =="paper" and computer_pick=="rock":
        print("youu wonnnn!!!!!!hurrayyyy")
        user_wins=user_wins+1
    elif user_input =="scissor" and computer_pick=="paper":
        print("youu wonnnn!!!!!!hurrayyyy")
        user_wins=user_wins+1
    else:
        print("computerrrrr winssss!!")
        computer_wins+=1

print("you won:",user_wins,"times.")
print("byeeeeee!!!!!hope you enjoyed the game")
