import pygame as p

screen = p.display.set_mode((800, 600))
p.display.set_caption("casino basis")

# Load image
platform = p.image.load ("Tokyo Ghoul.png")

# Main loop
running = True
clock = p.time.Clock()
while running == True:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    screen.blit(platform, (0, 0))
    p.display.flip()
    clock.tick(60)

player_pos = [100, 100]
player_speed = 4
player_size = 32
walking = False
walk_frame = 0

p.quit()