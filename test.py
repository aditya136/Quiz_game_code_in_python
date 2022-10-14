import pygame
from pygame import mixer


WIDTH, HEIGHT = 900, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Quiz game made by @aditya136")



icon = pygame.image.load('ideas.png')

pygame.display.set_icon(icon)

WIN.fill((0, 0, 0))

def draw_window():
    pygame.display.update()

FPS = 60





def main():
    clock = pygame.time.Clock()
    run = True
    while run:
         
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

       
       

    pygame.quit()

if __name__ == "__main__":
    main()
