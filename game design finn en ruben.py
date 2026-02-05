import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Casino")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 22)

# ------------------ KLEUREN ------------------
BG = (15, 15, 25)
NEON = (0, 255, 200)
RED = (200, 40, 40)
WHITE = (240, 240, 240)

# ------------------ PLAYER ------------------
player_pos = [100, 100]
player_speed = 4
player_size = 32
walking = False
walk_frame = 0

# ------------------ GAME STATE ------------------
chips = 1000
current_screen = "map"  # map, slot, roulette, coin, dice, shop, inventory
message = ""

inventory = []
equipped_shirt = "Groen shirt"
equipped_pants = "Groene broek"

# ------------------ INTERACTABLE OBJECTS ------------------
objects = {
    "slot": pygame.Rect(200, 200, 80, 80),
    "roulette": pygame.Rect(350, 200, 80, 80),
    "coin": pygame.Rect(500, 200, 80, 80),
    "dice": pygame.Rect(650, 200, 80, 80),
    "shop": pygame.Rect(800, 200, 80, 80),
}

# ------------------ HULPFUNCTIES ------------------


pygame.quit()
