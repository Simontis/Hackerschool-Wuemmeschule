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
