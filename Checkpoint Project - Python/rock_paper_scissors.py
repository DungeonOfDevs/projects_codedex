# Secund Version after the whole Python Course

import random

print('''
================================
Rock Paper Scissors Lizard Spock
================================
''')

symbols = {1: "✊", 2: "✋", 3: "✌️", 4: "🦎", 5: "🖖"}

print("1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖")

try:
    player = int(input("Pick a number (1-5): "))
    if player not in symbols:
        print("Sheldon is not happy that you are trying to break the rules!")
        exit()
except ValueError:
    print("Sheldon is wondering if you know what a number is?")
    exit()

computer = random.randint(1, 5)

print(f"Player:   {symbols[player]}")
print(f"Computer: {symbols[computer]}")


if player == computer:
    print("It's a Tie!")
elif (player == 1 and computer in [3, 4]) or \
        (player == 2 and computer in [1, 5]) or \
        (player == 3 and computer in [2, 4]) or \
        (player == 4 and computer in [2, 5]) or \
        (player == 5 and computer in [1, 3]):
    print("Player wins!")
else:
    print("Computer wins!")
