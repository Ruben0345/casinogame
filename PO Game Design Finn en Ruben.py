import pygame as p
import time
import random

p.init()
dobbelspel_status = "bet"
gewonnen_dobbelspel = False
gegooid = False
uitbetaald = False
bet = 0
choice = 0
geld = 1000
screen = p.display.set_mode((736, 600))
p.display.set_caption("casino basis")
p.mixer.init()
p.mixer.music.load("audio.mp3")
p.mixer.music.play(-1)

game_state = "main"
# Load image
platform = p.image.load ("Tokyo Ghoul.png")
dobbelsteen=p.image.load ("dobbelsteen.png")
Shop=p.image.load ("Shop.png")
dobbelsteen=p.transform.scale(dobbelsteen, (50,50))
Shop=p.transform.scale(Shop, (100,100))
dobbelsteenachtergrond=p.image.load ("dobbelspel achtergrond.png")
dobbelsteenachtergrond=p.transform.scale(dobbelsteenachtergrond, (736,600))
Shop_achtergrond=p.image.load ("Shop int.png")
Shop_achtergrond=p.transform.scale(Shop_achtergrond, (736,600))
muntje=p.image.load ("muntje.png")
muntje=p.transform.scale(muntje, (40,40))
muntje_x=625
muntje_y=50
dobbelsteen_x=161
dobbelsteen_y=245
Shop_x = 610
Shop_y = 510
player_x = 100
player_y = 100
player_speed = 4
walking = False
walk_frame = 0
player = p.image.load("download.png")
player = p.transform.scale(player, (50,50))
font = p.font.SysFont(None, 36)
text = font.render("Welkom, loop naar een spel om het te spelen!", True, (255,255,255))

# Main loop
running = True
clock = p.time.Clock()
text_show_until = time.time() + 3 
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
    collidingdobbel = player.get_rect(topleft=(player_x, player_y)).colliderect(dobbelsteen.get_rect(topleft=(dobbelsteen_x, dobbelsteen_y)))
    if collidingdobbel and keys[p.K_e]:
        game_state = "dice"
    collidingshop = player.get_rect(topleft=(player_x, player_y)).colliderect(Shop.get_rect(topleft=(Shop_x, Shop_y)))
    if collidingshop and keys[p.K_e]:
        game_state = "shop"
    
    


    while game_state == "dice":
        keys = p.key.get_pressed()
        screen.blit(dobbelsteenachtergrond, (0, 0))
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        if dobbelspel_status == "bet":    
            screen.blit(font.render("kies hoeveel je wilt inzetten!", True, (255,255,255)), (200, 100))
            screen.blit(font.render("druk 'Z' voor 10", True, (255,255,255)), (300, 140))
            screen.blit(font.render("druk 'X' voor 20", True, (255,255,255)), (300, 180))
            screen.blit(font.render("druk 'C' voor 50", True, (255,255,255)), (300, 220))
            if keys[p.K_z]:
                bet = 10
                dobbelspel_status = "choice"
            if keys[p.K_x]:
                bet = 20
                dobbelspel_status = "choice"
            if keys[p.K_c]:
                bet = 50
                dobbelspel_status = "choice"
            if bet > geld:
                screen.blit(font.render("Je hebt niet genoeg geld!", True, (255,0,0)), (200, 300))
                bet = 0
                time.sleep(4)
                p.display.flip()
                game_state = "main"
            
        elif dobbelspel_status == "choice":
            screen.blit(font.render("op welk cijfer wil je inzetten? druk 1 t/m 6", True, (255,255,255)), (200, 100))
            if keys[p.K_1]: choice = 1 
            if keys[p.K_2]: choice = 2 
            if keys[p.K_3]: choice = 3 
            if keys[p.K_4]: choice = 4 
            if keys[p.K_5]: choice = 5 
            if keys[p.K_6]: choice = 6 
            if choice != 0:
                dobbelspel_status = "result"
        elif dobbelspel_status == "result":
            if not gegooid:
                roll = random.randint(1,6)
                gegooid = True 
            elif not uitbetaald:
                if roll == choice:
                    gewonnen_dobbelspel = True 
                    geld += bet * 5
                else:
                    geld -= bet
                    gewonnen_dobbelspel = False
                uitbetaald = True
            if gewonnen_dobbelspel:
                screen.blit(font.render(f"Je hebt gewonnen! Het cijfer was {roll}", True, (0,255,0)), (200, 300))
            elif not gewonnen_dobbelspel:
               screen.blit(font.render(f"Je hebt verloren! Het cijfer was {roll}", True, (255,0,0)), (200, 300)) 
            screen.blit(font.render("Druk ESC om terug te gaan naar de map", True, (255,255,255)), (200, 100))
            screen.blit(font.render("Druk ENTER om opnieuw te spelen", True, (255,255,255)), (200, 140))

            if keys[p.K_RETURN]:
                    result_time = p.time.get_ticks()
                    bet = 0
                    gewonnen_dobbelspel = False
                    choice = 0
                    gegooid = False
                    uitbetaald = False
                    dobbelspel_status = "bet"
            if keys[p.K_ESCAPE]:
                    bet = 0
                    gewonnen_dobbelspel = True
                    choice = 0
                    gegooid = False
                    uitbetaald = False
                    dobbelspel_status = "bet"
                    game_state = "main"
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        p.display.flip()
        clock.tick(60)
    
    while game_state == "shop":
        keys = p.key.get_pressed()
        screen.blit(Shop_achtergrond, (0, 0))
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        screen.blit(font.render("Druk ESC om terug te gaan naar de map", True, (255,255,255)), (200, 100))
        if keys[p.K_ESCAPE]:
            game_state = "main"
        p.display.flip()
        clock.tick(60)

    screen.blit(platform, (0, 0))
    screen.blit(dobbelsteen, (dobbelsteen_x,dobbelsteen_y))
    screen.blit(Shop, (Shop_x, Shop_y))
    screen.blit(muntje, (muntje_x,muntje_y))
    geld_rechtsboven = font.render(str(geld), True, (255,255,255))
    screen.blit(geld_rechtsboven, (665, 58))
    screen.blit(player, (player_x,player_y))
    if time.time() < text_show_until:
        screen.blit(text, (20, 20))

    if collidingdobbel:
        screen.blit(font.render("Druk E om te spelen", True, (255,255,0)), (20, 60))
    if collidingshop:
        screen.blit(font.render("Druk E om te openen", True, (255,255,0)), (20, 60))


    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    p.display.flip()
    clock.tick(60)

p.quit()