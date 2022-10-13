import pygame
import os
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Quiz game made by @aditya1366')

WIDTH = (255, 255, 255)
HEIGHT = (0, 0, 0)
RED = (255, 255,0)
YELLOW = (255, 255, 0)

# BORDER = pygame.Rect(WIDTH//2 - 5,0, 10, HEIGHT)

if __name__ == "__main__":
    main()
