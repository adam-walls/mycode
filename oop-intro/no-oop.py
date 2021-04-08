#!/usr/bin/env python3
import random

player1_dice = []
player2_dice = []

for i in range(3):
  player1_dice.append(random.randint(1,6))
  player2_dice.append(random.randint(1,6))

# print results of each player's dice roll
print(f"Player 1 rolled {player1_dice}")
print(f"Player 2 rolled {player2_dice}")

if sum(player1_dice) == sum(player2_dice):
  print("Draw")
elif sum(player1_dice) > sum(player2_dice):
  print("Player 1 wins")
else:
  print("Player 2 wins")

