import pygame as p

screen = p.display.set_mode((800, 600))
p.display.set_caption("casino basis")

# Load image
platform = p.image.load ("Tokyo Ghoul.png")

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
    if keys[p.K_RIGHT] and player_x<680: 
        player_x += player_speed
    if keys[p.K_UP] and player_y<180: 
        player_y -= player_speed
    if keys[p.K_DOWN] and player_x>0: 
        player_y += player_speed

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    
    screen.blit(platform, (0, 0))
    screen.blit(player, (player_x,player_y))
    p.display.flip()
    clock.tick(60)


p.quit()