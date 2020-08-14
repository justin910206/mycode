from cheatdice import *
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
swapper_score = 0
loaded_dice_score = 0
number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
  swapper.roll()
  loaded_dice.roll()

  swapper.cheat()
  loaded_dice.cheat()


   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
 #print("Draw!")
    pass
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
 #print("Dice swapper wins!")
   swapper_score+= 1

  else:
 #print("Loaded dice wins!")
    loaded_dice_score += 1
  game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
if swapper_score == loaded_dice_score:
  print("Game was drawn")
elif swapper_score > loaded_dice_score:
  print("Swapper won most games")
else:
  print("Loaded dice won most games")\

class Cheat_Senescent_Pirate(Player):
    def cheat(self):
        print("Erm...let's see heare...")
        newvalue= randint(-10,10)
        newroll= randint(0,2)
        if newvalue < 1:
            print("Arggh, ye dunnit agin!")
            self.dice[newroll] = newvalue
        elif newvalue < 4:
            print("Cor blimey mate!")
            self.dice[newroll] = newvalue
        else:
            print("Scurvy-ridden timber flanks!")
            self.dice[newroll] = newvalue