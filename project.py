import random
def misty_graden():
    cornpitcher_position = 0
    cornpitcher_hp=10
    zombie_positon = -20
    zombie_hp=15
import time

# 游戏设置
SCREEN_WIDTH = 20
SCREEN_HEIGHT = 5
PLANT_POSITION = 1
ZOMBIE_POSITION = SCREEN_WIDTH - 1
ZOMBIE_SPEED = 1
PEA_SPEED = 1

def draw_screen(plant_pos, zombie_pos, peas):
    """ 绘制屏幕 """
    screen = [" " * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]
    # 放置植物
    screen[SCREEN_HEIGHT - 1] = " " * plant_pos + "P" + " " * (SCREEN_WIDTH - plant_pos - 1)
    
    # 放置僵尸
    screen[0] = " " * zombie_pos + "Z" + " " * (SCREEN_WIDTH - zombie_pos - 1)

    # 放置豌豆
    for pea in peas:
        if pea[1] == SCREEN_HEIGHT - 1:
            screen[pea[1]] = screen[pea[1]][:pea[0]] + "*" + screen[pea[1]][pea[0]+1:]

    print("\n".join(screen))

def move_peas(peas):
    """ 更新豌豆的位置 """
    new_peas = []
    for pea in peas:
        new_x = pea[0] + PEA_SPEED
        if new_x < SCREEN_WIDTH:
            new_peas.append((new_x, pea[1]))
    return new_peas

def check_collision(peas, zombie_pos):
    """ 检查豌豆是否与僵尸碰撞 """
    for pea in peas:
        if pea[0] == zombie_pos:
            return True
    return False

def game_loop():
    """ 游戏主循环 """
    plant_pos = PLANT_POSITION
    zombie_pos = ZOMBIE_POSITION
    peas = []
    
    while True:
        if choice == 8:
           PeaShooter_positon =-1

        if choice ==9:
            cornpitcher_pcoosition=1
          
        if choice ==0:
            sunflower_postition=1
        if choice == 2:
        print( Peashoote"        # 获取用户输入
        action = input("Press 'space' to shoot, 'a' to move left, 'd' to move right, 'q' to quit: ").lower()
        
        # 用户输入控制
        if action == "q":
            print("Game Over!")
            break
        elif action == "a" and plant_pos > 0:
            plant_pos -= 1
        elif action == "d" and plant_pos < SCREEN_WIDTH - 1:
            plant_pos += 1
        elif action == " ":
            peas.append((plant_pos + 1, SCREEN_HEIGHT - 1))  # 射击

        # 移动豌豆
        peas = move_peas(peas)

        # 检查豌豆与僵尸碰撞
        if check_collision(peas, zombie_pos):
            print("Zombie is hit!")
            break

        # 移动僵尸
        zombie_pos -= ZOMBIE_SPEED
        if zombie_pos <= 0:
            print("Zombie reached the plant! Game Over!")
            break
        
        # 绘制游戏屏幕
        draw_screen(plant_pos, zombie_pos, peas)

        time.sleep(0.5)  # 控制游戏速度

# 启动游戏
if __name__ == "__main__":
    game_loop()
 
