import pygame
import sys

pygame.init()  


WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("植物大战僵尸")

class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y, plant_type):
        super().__init__()
        self.rect = pygame.Rect(x, y, 50, 50)  
        self.type = plant_type

    def update(self):
        
        pass

    def draw(self, surface):
        if self.type == "sunflower":
            pygame.draw.rect(surface, (255, 255, 0), self.rect)  
        elif self.type == "peashooter":
            pygame.draw.rect(surface, (0, 255, 0), self.rect)  
        elif self.type == "wallnut":
            pygame.draw.rect(surface, (139, 69, 19), self.rect)  
        elif self.type == "cherry_bomb":
            pygame.draw.rect(surface, (255, 0, 0), self.rect)  

            import pygame
import sys

pygame.init()  


WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("植物大战僵尸")

PLANT_TYPES = ["sunflower", "peashooter", "wallnut", "cherry_bomb"]
current_plant_index = 0


all_sprites = pygame.sprite.Group()


class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y, plant_type):
        super().__init__()
        self.rect = pygame.Rect(x, y, 50, 50)
        self.type = plant_type

    def update(self):
       
        pass

    def draw(self, surface):
        if self.type == "sunflower":
            pygame.draw.rect(surface, (255, 255, 0), self.rect)
        elif self.type == "peashooter":
            pygame.draw.rect(surface, (0, 255, 0), self.rect)
        elif self.type == "wallnut":
            pygame.draw.rect(surface, (139, 69, 19), self.rect)
        elif self.type == "cherry_bomb":
            pygame.draw.rect(surface, (255, 0, 0), self.rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_plant_index = 0
            elif event.key == pygame.K_2:
                current_plant_index = 1
            elif event.key == pygame.K_3:
                current_plant_index = 2
            elif event.key == pygame.K_4:
                current_plant_index = 3
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse_x, mouse_y = pygame.mouse.get_pos()
            plant_type = PLANT_TYPES[current_plant_index]
            plant = Plant(mouse_x, mouse_y, plant_type)
            all_sprites.add(plant)

    
    window.fill((255, 255, 255))

  
    all_sprites.update()

    for sprite in all_sprites:
        sprite.draw(window)

    
    pygame.display.flip()


pygame.quit()
sys.exit()

    
