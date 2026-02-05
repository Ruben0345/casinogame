import pygame as p

screen = p.display.set_mode((800, 600))
p.display.set_caption("casino basis")

# Load image
platform = p.image.load ("Tokyo Ghoul.png")

# Main loop
running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False