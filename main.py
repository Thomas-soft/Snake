# LANCEMENT DU JEU

import pygame
from game import Game
from cryptography.fernet import Fernet
import os

if not os.path.exists("./save"):
    os.mkdir("./save")

if not os.path.exists("./save/snake_key.key"):
    with open("./save/snake_key.key", "wb") as f:
        f.write(Fernet.generate_key())
if not os.path.exists("./save/snake_data.json"):
    f = open("./save/snake_data.json", "wb")
    f.close()

pygame.init()

WINDOW_WIDTH = pygame.display.Info().current_w
WINDOW_HEIGHT = pygame.display.Info().current_h

pygame.display.set_caption("Snake")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)

game = Game(window=window)
game.run()

pygame.quit()