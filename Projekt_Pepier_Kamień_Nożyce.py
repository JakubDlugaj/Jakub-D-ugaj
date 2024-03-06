import getpass
Player = input("Type your name here:")
print(Player)
Player_confirm = input("If your name is correct type Yes ")
if Player_confirm  == "Yes":
    print("You are selected as player 1")
else:
    print("Enter your name again")

Question = (input("Do you know the rules? type y for yes n for no  y/n "))
if Question == "y":
    print("Waiting for the Player 2")
elif Question == "n":
    print("Rules are: Rock wins against scissors; paper wins against rock; and scissors wins against paper.")
    print("Waiting for the Player 2")

Player2 = input("Second player Type your name here:")
print(Player2)
print("If your name is correct press enter")
input("")

print("You are selected as player 2")
Question = (input("Do you know the rules? type y for yes n for no  y/n" ))
if Question == "y":
    print("All players are ready")
elif Question == "n":
    print("Rules are: Rock wins against scissors; paper wins against rock; and scissors wins against paper.")
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

