import random
def misty_graden():
    player_position = 0
    zombie_positon = 20
    PeaShooter_positon =0
    goal_position=30

while player_position <= goal_position or  PeaShooter_positon < goal_position:
   print("zombies are coming ")
   computer_choice = random.choice(["1","2","3"])
   if 