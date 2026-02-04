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

def draw_text(text, x, y, color=WHITE):
    t = font.render(text, True, color)
    screen.blit(t, (x, y))

def bet_menu():
    return random.choice([1, 10, 100, 1000])

# ------------------ SLOT MACHINE ------------------

def slot_machine(theme):
    global chips, message

    bet = bet_menu()
    if chips < bet:
        message = "Niet genoeg chips!"
        return

    chips -= bet

    if theme == "element":
        symbols = ["Vuur", "Water", "Blad"]
        jackpot = "Vuur"
    elif theme == "egypt":
        symbols = ["Mummie", "Pharaoh", "Hieroglyph"]
        jackpot = "Mummie"
    else:
        symbols = ["7", "Kers", "Bar"]
        jackpot = "7"

    roll = [random.choice(symbols) for _ in range(3)]

    if roll.count(jackpot) == 3:
        chips += bet * 5
        message = f"JACKPOT! +{bet*5}"
    elif roll[0] == roll[1] == roll[2]:
        chips += bet * 2
        message = f"Gewonnen! +{bet*2}"
    else:
        message = "Verloren!"

# ------------------ ROULETTE ------------------

def roulette():
    global chips, message
    bet = bet_menu()
    if chips < bet:
        message = "Niet genoeg chips!"
        return

    chips -= bet
    number = random.randint(0, 36)
    if number % 2 == 0:
        chips += bet * 2
        message = f"Rood/Zwart winst! Nummer {number}"
    else:
        message = f"Verloren! Nummer {number}"

# ------------------ COIN TOSS ------------------

def coin_toss():
    global chips, message
    bet = bet_menu()
    if chips < bet:
        message = "Niet genoeg chips!"
        return

    chips -= bet
    if random.choice(["kop", "munt"]) == "kop":
        chips += bet * 2
        message = "Kop! Gewonnen!"
    else:
        message = "Verloren!"

# ------------------ DOBBELSTEEN ------------------

def dice_game():
    global chips, message
    bet = bet_menu()
    guess = random.randint(1, 6)

    if chips < bet:
        message = "Niet genoeg chips!"
        return

    chips -= bet
    roll = random.randint(1, 6)

    if roll == guess:
        chips += bet * 5
        message = f"Goed geraden! +{bet*5}"
    else:
        message = f"Fout. Het was {roll}"

# ------------------ SHOP / LOOTBOX ------------------

def open_lootbox():
    global inventory, message
    loot = random.choice([
        "Rood vlam shirt",
        "Blauw vlam shirt",
        "Groen shirt",
        "Groene broek",
        "Bruine broek",
        "Lichtblauwe broek"
    ])
    inventory.append(loot)
    message = f"Gekregen: {loot}"

# ------------------ TEKEN FUNCTIES ------------------

def draw_map():
    screen.fill(BG)

    for name, rect in objects.items():
        pygame.draw.rect(screen, NEON, rect, border_radius=10)
        draw_text(name.upper(), rect.x, rect.y - 25)

def draw_player():
    global walk_frame
    color = (50 + walk_frame * 20, 200, 120)
    pygame.draw.rect(screen, color, (*player_pos, player_size, player_size))

def draw_ui():
    draw_text(f"Chips: {chips}", WIDTH - 180, 20, NEON)
    draw_text(message, 20, HEIGHT - 40, WHITE)

# ------------------ GAME LOOP ------------------

running = True
while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    walking = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                player_rect = pygame.Rect(*player_pos, player_size, player_size)
                for name, rect in objects.items():
                    if player_rect.colliderect(rect):
                        if name == "slot":
                            slot_machine("classic")
                        elif name == "roulette":
                            roulette()
                        elif name == "coin":
                            coin_toss()
                        elif name == "dice":
                            dice_game()
                        elif name == "shop":
                            open_lootbox()

    # Movement
    if keys[pygame.K_w]:
        player_pos[1] -= player_speed
        walking = True
    if keys[pygame.K_s]:
        player_pos[1] += player_speed
        walking = True
    if keys[pygame.K_a]:
        player_pos[0] -= player_speed
        walking = True
    if keys[pygame.K_d]:
        player_pos[0] += player_speed
        walking = True

    if walking:
        walk_frame = (walk_frame + 1) % 10

    # Game over
    if chips <= 0:
        screen.fill((0, 0, 0))
        draw_text("GAME OVER - Geen chips meer", 300, 300, RED)
        pygame.display.update()
        continue

    draw_map()
    draw_player()
    draw_ui()

    pygame.display.update()

pygame.quit()
