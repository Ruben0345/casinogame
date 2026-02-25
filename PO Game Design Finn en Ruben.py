import pygame as p
import time
import random

#variabelen, gamestates en muziek hieronder
p.init()
dobbelspel_status = "bet"
Shop_status = "choice"
coinflip_status = "bet"
gewonnen_dobbelspel = False
gegooid = False
uitbetaald = False
shop_betaald = False
bet = 0
Kost_Box = 0
choice = 0
inventory = {
    "LuckyBox_G": 0,
    "LuckyBox_R": 0
}
loot_items_G = [
    ("Rood Shirt", "RSG.png"),
    ("Blauw Shirt", "BSG.png"),
    ("Paars Shirt", "PSG.png"),
    ("Groen Shirt", "GRSG.png"),
    ("Geel Shirt", "GESG.png")
]
spin_x = 0
spin_speed = 40
spinning = True
start_x = 100
y = 250
spacing = 100
spin_end_time = None
geld = 1000
gewonnen_item = None
center_x = 736 // 2
screen = p.display.set_mode((736, 600))
p.display.set_caption("casino basis")
p.mixer.init()
p.mixer.music.load("audio.mp3")
p.mixer.music.play(-1)
game_state = "main"
roulette_status = "bet"
roulette_bet = 0
roulette_choice = None
roulette_result = None
roulette_spinning = False
roulette_angle = 0
roulette_speed = 0
roulette_uitbetaald = False
# foto's enzo hieronder
platform = p.image.load ("Tokyo Ghoul.png")
dobbelsteen=p.image.load ("dobbelsteen.png")
Shop=p.image.load ("Shop.png")
dobbelsteen=p.transform.scale(dobbelsteen, (50,50))
Shop=p.transform.scale(Shop, (100,100))
dobbelsteenachtergrond=p.image.load ("dobbelspel achtergrond.png")
dobbelsteenachtergrond=p.transform.scale(dobbelsteenachtergrond, (736,600))
Shop_achtergrond=p.image.load ("Shop int.png")
Shop_achtergrond=p.transform.scale(Shop_achtergrond, (736,600))
Shop_achtergrond_G=p.image.load ("Shop int_G.png")
Shop_achtergrond_G=p.transform.scale(Shop_achtergrond_G, (736,600))
Shop_achtergrond_R=p.image.load ("Shop int_R.png")
Shop_achtergrond_R=p.transform.scale(Shop_achtergrond_R, (736,600))
gBox = p.image.load("LB_G.png")
rBox = p.image.load("LB_R.png")
loaded_items_G = []
for rarity, img in loot_items_G:
    image = p.image.load(img)
    image = p.transform.scale(image, (80,80))
    loaded_items_G.append((rarity, image))
spin_items_G = []
for i in range(50):
    spin_items_G.append(random.choice(loaded_items_G))
Placeholder = p.image.load("Place holder.png")
muntje=p.image.load ("muntje.png")
muntje=p.transform.scale(muntje, (40,40))
muntje_x=625
muntje_y=50
coinflipA=p.image.load("coinflip.png")
coinflipA=p.transform.scale(coinflipA, (50,50))
coinflipA_x=227
coinflipA_y=435
coinflipscherm=p.image.load("coinflipscherm.png")
coinflipscherm=p.transform.scale(coinflipscherm, (736,600))
coinflipkop=p.image.load("coinflip kop.png")
coinflipkop=p.transform.scale(coinflipkop, (736,600))
coinflipmunt=p.image.load("coinflip munt.png")
coinflipmunt=p.transform.scale(coinflipmunt, (736,600))
rouletteplatform=p.image.load("roulette platform.png")
rouletteplatform=p.transform.scale(rouletteplatform, (50,50))
rouletteplatform_x=467
rouletteachtergrond=p.image.load("roulette achtergrond.png")
rouletteachtergrond=p.transform.scale(rouletteachtergrond, (736,600))
rouletteplatform_y=267
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

# main loop hieronder
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
    collidngcoinflip = player.get_rect(topleft=(player_x, player_y)).colliderect(coinflipA.get_rect(topleft=(coinflipA_x, coinflipA_y)))
    if collidngcoinflip and keys[p.K_e]:
        game_state = "coinflip"
    if keys[p.K_i]:
        game_state = "inventory_B"
    collidingroulette = player.get_rect(topleft=(player_x, player_y)).colliderect(rouletteplatform.get_rect(topleft=(rouletteplatform_x, rouletteplatform_y)))
    if collidingroulette and keys[p.K_e]:
        game_state = "roulette"

    while game_state == "roulette":
        keys = p.key.get_pressed()
        screen.blit(rouletteachtergrond, (0, 0))
        
        
        
        
        
        
        
        
        
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        if keys[p.K_ESCAPE]:
            game_state = "main"
        p.display.flip()
        clock.tick(60)

    while game_state == "coinflip":
        keys = p.key.get_pressed()
        screen.blit(coinflipscherm, (0, 0))
        if coinflip_status == "bet":
            screen.blit(font.render("kies hoeveel je wilt inzetten!", True, (255,255,0)), (200, 100))
            screen.blit(font.render("druk 'Z' voor 10", True, (255,255,0)), (300, 140))
            screen.blit(font.render("druk 'X' voor 20", True, (255,255,0)), (300, 180))
            screen.blit(font.render("druk 'C' voor 50", True, (255,255,0)), (300, 220))
            if keys[p.K_z]:
                bet = 10
            if keys[p.K_x]:
                bet = 20
            if keys[p.K_c]:
                bet = 50
            elif bet > geld:
                screen.blit(font.render("Je hebt niet genoeg geld!", True, (255,0,0)), (200, 300))
                bet = 0
                coinflip_status = "bet"
                time.sleep(4)
                p.display.flip()
                game_state = "main"
            elif bet<= geld and bet != 0:
                coinflip_status = "choice"
        elif coinflip_status == "choice":
            screen.blit(font.render("kies kop of munt! druk K voor kop en M voor munt", True, (255,255,0)), (200, 100))
            if keys[p.K_k]: choice = "kop" 
            if keys[p.K_m]: choice = "munt" 
            if choice != 0:
                coinflip_status = "result"
        elif coinflip_status == "result":
            if not gegooid:
                flip = random.choice(["kop", "munt"])
                gegooid = True
            if flip == "kop":
                coinflip_status = "result_kop"
            if flip == "munt":
                coinflip_status = "result_munt"
        elif coinflip_status == "result_kop":
            screen.blit(coinflipkop, (0, 0))
            if choice == "kop":
                screen.blit(font.render("Je hebt gewonnen!", True, (0,255,0)), (200, 300))
                if not uitbetaald:
                    geld += bet
                    uitbetaald = True
            else:
                screen.blit(font.render("Je hebt verloren!", True, (255,0,0)), (200, 300)) 
                if not uitbetaald:
                    geld -= bet
                    uitbetaald = True
            screen.blit(font.render("Druk ESC om terug te gaan naar de map", True, (255,255,255)), (200, 100))
            screen.blit(font.render("Druk ENTER om opnieuw te spelen", True, (255,255,255)), (200, 140))

            if keys[p.K_RETURN]:
                    result_time = p.time.get_ticks()
                    bet = 0
                    choice = 0
                    gegooid = False
                    uitbetaald = False
                    coinflip_status = "bet"
            if keys[p.K_ESCAPE]:
                    bet = 0
                    choice = 0
                    gegooid = False
                    uitbetaald = False
                    coinflip_status = "bet"
                    game_state = "main"
        elif coinflip_status == "result_munt":
            screen.blit(coinflipmunt, (0, 0))
            if choice == "munt":
                screen.blit(font.render("Je hebt gewonnen!", True, (0,255,0)), (200, 300))
                if not uitbetaald:
                    uitbetaald = True
                    geld += bet
                    uitbetaald = True
            else:
                screen.blit(font.render("Je hebt verloren!", True, (255,0,0)), (200, 300)) 
                if not uitbetaald:
                    geld -= bet
                    uitbetaald = True
            screen.blit(font.render("Druk ESC om terug te gaan naar de map", True, (255,255,255)), (200, 100))
            screen.blit(font.render("Druk ENTER om opnieuw te spelen", True, (255,255,255)), (200, 140))

            if keys[p.K_RETURN]:
                    result_time = p.time.get_ticks()
                    bet = 0
                    choice = 0
                    gegooid = False
                    uitbetaald = False
                    coinflip_status = "bet"
            if keys[p.K_ESCAPE]:
                    bet = 0
                    choice = 0
                    gegooid = False
                    uitbetaald = False
                    coinflip_status = "bet"
                    game_state = "main"
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        p.display.flip()
        clock.tick(60)

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
            if keys[p.K_x]:
                bet = 20
            if keys[p.K_c]:
                bet = 50
            elif bet > geld:
                screen.blit(font.render("Je hebt niet genoeg geld!", True, (255,0,0)), (200, 300))
                bet = 0
                dobbelspel_status = "bet"
                time.sleep(4)
                p.display.flip()
                game_state = "main"
            elif bet<= geld and bet != 0:
                dobbelspel_status = "choice"
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
        
    while game_state == "inventory_B":

        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

        keys = p.key.get_pressed()
        
        screen.fill((30,30,30))

        title = font.render("Inventory", True, (255,255,255))
        screen.blit(title, (300,50))

        screen.blit(gBox, (-50,-50))
        screen.blit(rBox, (150,-50))
        screen.blit(font.render(str(inventory["LuckyBox_G"]), True, (255,255,255)), (250,250))
        screen.blit(font.render(str(inventory["LuckyBox_R"]), True, (255,255,255)), (450,250))

        Open_G = font.render("Durk op G om een Gouden Lucky Box te openen", True, (255,255,255))
        Open_R = font.render("Durk op R om een Regenboog Lucky Box te openen", True, (255,255,255))
        Open_KI = font.render("Druk op E om je Kleding inventory te openen", True, (255,255,255))
        screen.blit(Open_G,(80, 300))
        screen.blit(Open_R,(60, 375))
        screen.blit(Open_KI, (100, 450))
        exit_text = font.render("Of druk ESC om te sluiten", True, (255,255,255))
        screen.blit(exit_text, (230,525))

        if keys[p.K_g] and (inventory["LuckyBox_G"]) > 0:
            game_state = "op_G"
        if keys[p.K_r] and (inventory["LuckyBox_R"]) > 0:
            game_state = "op_R"
        if keys[p.K_e]:
            game_state = "op_I"
        if keys[p.K_ESCAPE]:
            game_state = "main"

        p.display.flip()
        clock.tick(60) 

    while game_state == "shop":

        keys = p.key.get_pressed()
        screen.blit(Shop_achtergrond, (0, 0))
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

        if keys[p.K_ESCAPE]:
                Shop_status="choice"
                game_state = "main"

        if Shop_status == "choice":    
            screen.blit(font.render("Je kan tussen twee Lucky boxes kiezen", True, (255,255,255)), (150, 10))
            screen.blit(font.render("Voor een een goude van €500 druk 1", True, (255,255,255)), (150, 50))
            screen.blit(font.render("En voor een een regenboog van €1000 druk 2", True, (255,255,255)), (150, 90))
            screen.blit(font.render("Druk ESC om terug te gaan naar de map", True, (255,255,255)), (150, 500))
            if keys[p.K_1]:
                Kost_Box = 500
                Shop_status = "recieved_G"
            if keys[p.K_2]:
                Kost_Box = 1000
                Shop_status = "recieved_R"
            if geld < Kost_Box:
                screen.blit(font.render("Je hebt niet genoeg geld!", True, (255,0,0)), (150, 40))
                Kost_Box = 0
                time.sleep(4)
                p.display.flip()
                game_state = "main"
        elif Shop_status == "recieved_G":
            screen.blit(Shop_achtergrond_G, (0, 0))
            screen.blit(font.render("Een Goude Lucky Box zit nu in je inventory", True, (255,255,255)), (150, 40))
            screen.blit(font.render("Klik op enter om door te gaan", True, (255,255,255)), (150, 80))
            if not shop_betaald:
                inventory["LuckyBox_G"] += 1
                geld -= 500
                shop_betaald = True
            if keys[p.K_RETURN]:
                shop_betaald = False
                Shop_status = "choice"
                game_state = "main" 

        elif Shop_status == "recieved_R":
            screen.blit(Shop_achtergrond_R, (0, 0))
            screen.blit(font.render("Een Regenboog Lucky Box zit nu in je inventory", True, (255,255,255)), (150, 40))
            screen.blit(font.render("Klik op enter om door te gaan", True, (255,255,255)), (150, 80))
            if not shop_betaald:
                inventory["LuckyBox_R"] += 1
                geld -= 500
                shop_betaald = True
            if keys[p.K_RETURN]:
                shop_betaald = False
                Shop_status = "choice" 
                game_state = "main"

        
        p.display.flip()
        clock.tick(60)

    while game_state == "op_G":

        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        target_index = random.randint(10, len(spin_items_G)-10)
        target_item = spin_items_G[target_index]
        target_x = start_x + target_index * spacing
        stop_position = center_x - target_x
        screen.fill((20,20,20))

        for i, item in enumerate(spin_items_G):
            img = item[1]
            x = 100 + i*100 + spin_x
            screen.blit(img, (x,250))

        if spinning:
            spin_x -= spin_speed
            spin_speed *= 0.97

            if spin_x <= stop_position:
                spin_x = stop_position
                spinning = False
                gewonnen_item = target_item
                spin_end_time = p.time.get_ticks()
        
        if not spinning and spin_end_time:
            if p.time.get_ticks() - spin_end_time > 2000:
                inventory["LuckyBox_G"] -= 1
                spinning = True
                spin_speed = 40
                spin_x = 0
                gewonnen_item = None
                spin_end_time = None
                game_state = "inventory_B"

        if gewonnen_item:
            screen.blit(font.render( gewonnen_item[0], True, (255,0,0)), (150, 40))
        p.draw.rect(screen, (255,255,0), (368,230,5,120))

        p.display.flip()
        clock.tick(60)
    
        

    screen.blit(platform, (0, 0))
    screen.blit(dobbelsteen, (dobbelsteen_x,dobbelsteen_y))
    screen.blit(Shop, (Shop_x, Shop_y))
    screen.blit(muntje, (muntje_x,muntje_y))
    screen.blit(rouletteplatform, (rouletteplatform_x, rouletteplatform_y)) 
    screen.blit(coinflipA, (coinflipA_x, coinflipA_y))
    geld_rechtsboven = font.render(str(geld), True, (255,255,255))
    screen.blit(geld_rechtsboven, (665, 58))
    screen.blit(player, (player_x,player_y))
    if time.time() < text_show_until:
        screen.blit(text, (20, 20))
    if collidingroulette:
        screen.blit(font.render("Druk E om te spelen", True, (255,255,0)), (20, 60))
    if collidingdobbel:
        screen.blit(font.render("Druk E om te spelen", True, (255,255,0)), (20, 60))
    if collidingshop:
        screen.blit(font.render("Druk E om te openen", True, (255,255,0)), (20, 60))
    if collidngcoinflip:
        screen.blit(font.render("Druk E om te spelen", True, (255,255,0)), (20, 60))

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    p.display.flip()
    clock.tick(60)

p.quit()