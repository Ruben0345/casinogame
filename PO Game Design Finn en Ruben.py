import pygame as p
import time
import random

geld = 1000

screen = p.display.set_mode((736, 600))
p.display.set_caption("casino basis")
p.mixer.init()
p.mixer.music.load("audio.mp3")
p.mixer.music.play(-1)


# Load image
platform = p.image.load ("Tokyo Ghoul.png")
dobbelsteen=p.image.load ("dobbelsteen.png")
dobbelsteen=p.transform.scale(dobbelsteen, (50,50))

dobbelsteen_x=161
dobbelsteen_y=245
player_x = 100
player_y = 100
player_speed = 4
walking = False
walk_frame = 0
player = p.image.load("download.png")
player = p.transform.scale(player, (50,50))

# Main loop
running = True
clock = p.time.Clock()
while running == True:
    keys = p.key.get_pressed() 
    if keys[p.K_LEFT] and player_x>0: 
        player_x -= player_speed
    if keys[p.K_RIGHT] and player_x<670: 
        player_x += player_speed
    if keys[p.K_UP] and player_y>0: 
        player_y -= player_speed
    if keys[p.K_DOWN] and player_y<550 : 
        player_y += player_speed


    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    
    screen.blit(platform, (0, 0))
    screen.blit(dobbelsteen, (dobbelsteen_x,dobbelsteen_y))
    screen.blit(player, (player_x,player_y))

    p.display.flip()
    clock.tick(60)


p.quit()