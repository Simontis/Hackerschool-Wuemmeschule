import random

print("Schere, Stein, Papier")

choices = ["Schere", "Stein", "Papier"]

while True:
    player_choice = input("Deine Wahl: ")
    computer_choice = random.choice(choices)

    print("Computer wählt: " + computer_choice)

    if player_choice == computer_choice:
        print("Unentschieden!")
    elif player_choice == "Schere" and computer_choice == "Papier":
        print("Du gewinnst!")
    elif player_choice == "Stein" and computer_choice == "Schere":
        print("Du gewinnst!")
    elif player_choice == "Papier" and computer_choice == "Stein":
        print("Du gewinnst!")
    else:
        print("Computer gewinnt!")
