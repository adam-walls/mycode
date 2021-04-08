#!/user/bin/env python3 

# Inherit the classes from cheatdice.py
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

# Turns cheater1's last dice roll into a guaranteed 6
cheater1 = Cheat_Swapper()
# Increases cheater2's rolls by 1
cheater2 = Cheat_Loaded_Dice()

# Get dice rolls for cheater1 and cheater2
cheater1.roll()
cheater2.roll()

# Apply respective cheats to each cheater's dice
cheater1.cheat() # Cheat_Swapper()
cheater2.cheat() # Cheat_Loaded_Dice()   

# Display dice rolls
print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

# Calculate and display who won
if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
  print("Draw!")

elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
  print("Cheater 1 wins!")

else:
  print("Cheater 2 wins!")
