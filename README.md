# Hackerschool-Wuemmeschule

Hallo, 

falls ihr die Dateien herunterladen möchtet, klickt oben einfach auf den grünen Button, auf dem "Code" steht.

Dann unten könnt ihr unten in dem Menü "download ZIP" auswälen.

Anschließend müsst ihr diese ZIP-Datei nur über einen Rechtsklick entpacken, die Dateien öffnen und anschließend den darin enthaltenen Text (Code) in euer
Replit kopieren.

Für die, die die Dateien nicht herunterladen möchten, hier nochmal der Code. Viel Spaß!:



#Zahlen raten#
import random

print("Willkommen bei 'Zahlen erraten'!")
number = random.randint(1, 100)
guess = 0
tries = 0

while guess != number:
    guess = int(input("Gib eine Zahl zwischen 1 und 100 ein: "))
    tries += 1

    if guess < number:
        print("Zu niedrig!")
    elif guess > number:
        print("Zu hoch!")
    else:
        print("Richtig geraten in", tries, "Versuchen!")
       
       
       
       
#Schere, Stein, Papier#
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
