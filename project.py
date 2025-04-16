import random
import time


screen_width = 20
screen_hidth = 5
plant_pos = 5
zombie_pos = screen_width - 1
zombie_SPEED = 1
dpea_speed = 1

def draw_screen(plant_pos, zombie_pos, peas):
    
    screen = [" " * screen_width for _ in range(plant_pos or zombie_pos)]
    
    screen_hidth = " " * plant_pos + "P" + " " * (screen_width - plant_pos - 1)
    
   
    screen[0] = " " * zombie_pos + "Z" + " " * (screen_width - zombie_pos - 1)

   
    for pea in peas:
        if pea[1] == screen_hidth- 1:
            screen[pea[1]] = screen[pea[1]][:pea[0]] + "*" + screen[pea[1]][pea[0]+1:]

    print("\n".join(screen))

def move_peas(peas):
   
    new_peas = []
    for pea in peas:
        new_x = pea[0] + dpea_speed
        if new_x < screen_width:
            new_peas.append((new_x, pea[1]))
    return new_peas

def check_collision(peas, zombie_pos):
  
    for pea in peas:
        if pea[0] == zombie_pos:
            return True
    return False

def game_loop():
 
    plant_pos=screen_hidth
    zombie_pos=screen_hidth
    peas = []
    
    while True:
       
        action = input("Press 'f' to shoot, 'a' to move left, 'd' to move right, 'q' to quit: ").lower()
        
      
        if action == "q":
            print("Game Over!")
            break
        elif action == "a" and plant_pos > 0:
            plant_pos -= 1
        elif action == "d" and plant_pos < screen_width - 1:
            plant_pos += 1
        elif action == "f":
            peas.append((plant_pos + 1, screen_hidth - 1))  

      
        peas = move_peas(peas)

                
        if check_collision(peas, zombie_pos):
            print("Zombie is hit!")
            break

       
        zombie_pos -= zombie_SPEED
        if zombie_pos <= 0:
            print("Zombie reached the plant! Game Over!")
            break
        
        
        draw_screen(plant_pos, zombie_pos, peas)

        time.sleep(0.5) 


if __name__ == "__main__":
    game_loop()
 
