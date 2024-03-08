import getpass
Player = input("Type your name here:")
print(Player)

correct_name = False
while not correct_name:
    Player_confirm = input("If your name is correct, type Yes: ")
    if Player_confirm.lower() == "yes":
        correct_name = True
    else:
        Player = input("Enter your name again: ")
        print(Player)

print("You are selected as player 1")


print("Rules are: Rock wins against scissors; paper wins against rock; and scissors wins against paper. Player that will win 3 times is a winner ")        
def Question():
    Question = (input("IF you khnow the rules and did read them above than press any key to start"))

Player2 = input("Second player Type your name here:")
print(Player2)

correct_name = False
while not correct_name:
    Player_confirm = input("If your name is correct, type Yes: ")
    if Player_confirm.lower() == "yes":
        correct_name = True
    else:
        Player = input("Enter your name again: ")
        print(Player)
print("You are selected as player 2")

Question()


print("All players are ready")

Player_Score = 0
Player2_Score = 0

Only_options = ["Rock", "Paper", "Scissors"]
while Player_Score != 3 and Player2_Score != 3:

    Player_Choice_correct = True
    while Player_Choice_correct:
        Player = getpass.getpass("Player 1, make your choice: ")
        if Player in Only_options:
            Player_Choice_correct = False

    Player_Choice_correct = True
    while Player_Choice_correct:
        Player2 = input("Player 2, make your choice: ")
        if Player2 in Only_options:
            Player_Choice_correct = False

    if Player == "Paper" and Player2 == "Rock" \
    or Player == "Rock" and Player2 == "Scissors" \
    or Player == "Scissors" and Player2 == "Paper":
        print("Player 1 has won this round")
        Player_Score += 1
    elif Player == Player2:
        print("It's a draw")
    else:
        print("Player 2 has won this round")
        Player2_Score += 1

if Player_Score > Player2_Score:
    print("Player 1 won the game")
else:
    print("Player 2 won the game")
