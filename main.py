import pygame, os, random


# Initialize pygame
pygame.init()

# Create the screen
width, height = 500, 500
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (600,200)
screen = pygame.display.set_mode((width, height))

# Background music
pygame.mixer_music.load("Music/Birds [NCS Realese].mp3")
pygame.mixer_music.set_volume(0.2)
pygame.mixer_music.play(-1)

# Title and icon
pygame.display.set_caption("Tic Tac Toe - Piškvorky (3x3)")
icon = pygame.image.load("IMG/tic-tac-toe.png")
pygame.display.set_icon(icon)


# Colours|RGB = Red, Green, Blue
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (150, 0, 0)
DARK_GREEN = (0, 80, 0)
VIOLET = (0, 0, 150)


# Languages
en, cz = True, False

def languages_fce(mouse_pos):
    global en, cz
    if mouse_pos[0] > xl and mouse_pos[0] < xl + lanx and mouse_pos[1] > yl and mouse_pos[1] < yl + lany:
        en = True
        cz = False
    elif mouse_pos[0] > xl and mouse_pos[0] < xl + lanx and mouse_pos[1] > yl + height//8 and mouse_pos[1] < yl + height//8 + lany:
        en = False
        cz = True


# Rules
def rules():
    x1, y1 = width / 10 * 4 - (width/25), height / 8
    pygame.draw.rect(screen, BLACK, (x1 - width/32, y1, 3*(width/8), height/7))
    rule_font = pygame.font.Font("Fonds/jack_font.TTF", 50)
    if en:
        rule_text = rule_font.render("RULES", True, WHITE)
        screen.blit(rule_text, (x1, y1))
    elif cz:
        rule_text = rule_font.render("PRAVIDLA", True, WHITE)
        screen.blit(rule_text, (x1 - width/10, y1))

    hei = 5*(height/8)
    pygame.draw.rect(screen, BLACK, (x1 - width/3, y1 + height/8, 15*(width/16), hei))
    rule_font = pygame.font.Font("Fonds/coolvetica.TTF", 30)

    if en:
        rule_text = rule_font.render("Game for two players", True, WHITE)
        screen.blit(rule_text, (x1 - 5*(width/32), y1 + height/8))
    elif cz:
        rule_text = rule_font.render("Hra pro dva hráče", True, WHITE)
        screen.blit(rule_text, (x1 - 3*(width/32), y1 + height/8))

    if en:
        rule_text = rule_font.render("players take turns", True, WHITE)
        screen.blit(rule_text, (x1 - 4*(width/32), y1 + height/4))
    elif cz:
        rule_text = rule_font.render("hráči se střídají po jednom tahu", True, WHITE)
        screen.blit(rule_text, (x1 - 8*(width/32), y1 + height/4))

    if en:
        rule_text = rule_font.render("Your goal is to get 3 times", True, WHITE)
        screen.blit(rule_text, (x1 - 7*(width/32), y1 + 3*(height/8)))
    elif cz:
        rule_text = rule_font.render("Tvým cílem je dostat vedle sebe", True, WHITE)
        screen.blit(rule_text, (x1 - width/4, y1 + 3*(height/8)))

    if en:
        rule_text = rule_font.render("same symbol in either", True, WHITE)
        screen.blit(rule_text, (x1 - 4*(width/27), y1 + 4*(height/8)))
    elif cz:
        rule_text = rule_font.render("3x stejnej symbol na jeden", True, WHITE)
        screen.blit(rule_text, (x1 - 6*(width/27), y1 + 4*(height/8)))

    if en:
        rule_text = rule_font.render("row, column or diagonal", True, WHITE)
        screen.blit(rule_text, (x1 - 7*(width/40), y1 + 5*(height/8)))
    elif cz:
        rule_text = rule_font.render("řádek, sloupec nebo diagonálu", True, WHITE)
        screen.blit(rule_text, (x1 - 7*(width/27), y1 + 5*(height/8)))


# Vlajky
def flags():
    global xl, yl, lanx, lany
    # Languages/flags 
    mouse_pos = pygame.mouse.get_pos()
    lanx, lany = width//10, height//10
    xl, yl = width - width/7, height/30
        # English
    en_pic = pygame.transform.scale(pygame.image.load("IMG/england.jpg"), (lanx, lany))
    screen.blit(en_pic, (xl, yl))
    if mouse_pos[0] > xl and mouse_pos[0] < xl + lanx and mouse_pos[1] > yl and mouse_pos[1] < yl + lany:
        dark_en = pygame.Surface(en_pic.get_size()).convert_alpha()
        dark_en.fill((0, 0, 0, 100))
        screen.blit(dark_en, (xl, yl))
        # Czech
    cz_pic = pygame.transform.scale(pygame.image.load("IMG/czech.png"), (lanx, lany))
    screen.blit(cz_pic, (xl, yl + height//8))
    if mouse_pos[0] > xl and mouse_pos[0] < xl + lanx and mouse_pos[1] > yl + height//8 and mouse_pos[1] < yl + height//8 + lany:
        dark_cz = pygame.Surface(cz_pic.get_size()).convert_alpha()
        dark_cz.fill((0, 0, 0, 100))
        screen.blit(dark_cz, (xl, yl + height//8))


# Checking if game is not end
def the_end():
    global end
    global winner
    # Line 1
    if m_1 == m_2 == m_3:
        end = True
        winner = m_1
    # Line 2
    elif m_4 == m_5 == m_6:
        end = True
        winner = m_4
    # Line 3
    elif m_7 == m_8 == m_9:
        end = True
        winner = m_7
    # Column 1
    elif m_1 == m_4 == m_7:
        end = True
        winner = m_1
    # Column 2
    elif m_2 == m_5 == m_8:
        end = True
        winner = m_2
    # Column 3
    elif m_3 == m_6 == m_9:
        end = True
        winner = m_3
    # Diagonal 1
    elif m_1 == m_5 == m_9:
        end = True
        winner = m_1
    # Dialgonal 2
    elif m_3 == m_5 == m_7:
        end = True
        winner = m_3
    elif m_1 != 1 and m_2 != 2 and m_3 != 3 and m_4 != 4 and m_5 != 5 and m_6 != 6 and m_7 != 7 and m_8 != 8 and m_9 != 9:
        end = True
        winner = None


# Computer move
def computer_move():
    may = []
    may2 = []
    for copy in ["O", "X"]:
        for i in range(9):
            copy_tabulka = [m_1, m_2, m_3, m_4, m_5, m_6, m_7, m_8, m_9]
            if copy_tabulka[i] != "O" and copy_tabulka[i] != "X":
                copy_tabulka[i] = copy
                if (copy_tabulka[0] == copy_tabulka[1] == copy_tabulka[2]) or (copy_tabulka[3] == copy_tabulka[4] == copy_tabulka[5]) or (copy_tabulka[6] == copy_tabulka[7] == copy_tabulka[8]) or (copy_tabulka[0] == copy_tabulka[3] == copy_tabulka[6]) or (copy_tabulka[1] == copy_tabulka[4] == copy_tabulka[7]) or (copy_tabulka[2] == copy_tabulka[5] == copy_tabulka[8]) or (copy_tabulka[0] == copy_tabulka[4] == copy_tabulka[8]) or (copy_tabulka[2] == copy_tabulka[4] == copy_tabulka[6]):
                    return i+1
                elif i == 4:
                    return i + 1
                elif i == 0 or i == 2 or i == 6 or i == 8:
                    may.append(i)
                else:
                    may2.append(i)
    if len(may) != 0:
        ran = random.randrange(0, len(may))
        number = may[ran]
    else:
        ran = random.randrange(0, len(may2))
        number = may2[ran]
    may.clear()
    may2.clear()
    return number + 1


def text_winner():
    if winner == None:
        x1, y1 = width / 10 * 4 - (width/50), height / 5 * 2
        winner_font = pygame.font.Font("Fonds/jack_font.TTF", 50)
        if en:
            pygame.draw.rect(screen, BLACK, (x1, y1, 2*(width/8), height/8))
            winner_text = winner_font.render("Tie", True, WHITE)
            screen.blit(winner_text, (x1 + width/20, y1))
        elif cz:
            pygame.draw.rect(screen, BLACK, (x1 - width/15, y1, 8*(width/20), height/8))
            winner_text = winner_font.render("Remíza", True, WHITE)
            screen.blit(winner_text, (x1 - width/20, y1))
    else:
        x2, y2 = width / 6, height / 5 * 2
        if en:
            pygame.draw.rect(screen, BLACK, (x2 - width/20, y2 - height/20, 5*(width/7), height/5))
            winner_font = pygame.font.Font("Fonds/jack_font.TTF", 50)
            winner_text = winner_font.render("Winner is "+ str(winner), True, WHITE)
            screen.blit(winner_text, (x2, y2))
        elif cz:
            pygame.draw.rect(screen, BLACK, (x2 + width/20, y2 - height/20, 4*(width/7), height/5))
            winner_font = pygame.font.Font("Fonds/coolvetica.TTF", 50)
            winner_text = winner_font.render("Vítěz  je  "+ str(winner), True, WHITE)
            screen.blit(winner_text, (x2 + width/10, y2))


# Restart button
def restart_button():
    mouse_pos = pygame.mouse.get_pos()
    x, y = width / 8 + 2*(width/8), height / 8 + 4*(height/8)
    if mouse_pos[0] > x and mouse_pos[0] < (width/8) + 4*(width/8) and mouse_pos[1] > y and mouse_pos[1] < (height/8) + 5*(height/8):
        pygame.draw.rect(screen, DARK_GREEN, (x, y, 2*(width/8), height/8))
        restart_font = pygame.font.Font("Fonds/jack_font.TTF", 30)
        if end:
            restart_text = restart_font.render("Restart", True, BLACK)
            screen.blit(restart_text, (x + width/80, y + height/30))
        elif not game:
            restart_text = restart_font.render("Start", True, BLACK)
            screen.blit(restart_text, (x + width/22, y + height/30))
    else:
        pygame.draw.rect(screen, GREEN, (x, y, 2*(width/8), height/8))
        restart_font = pygame.font.Font("Fonds/jack_font.TTF", 30)
        if end:
            restart_text = restart_font.render("Restart", True, BLACK)
            screen.blit(restart_text, (x + width/100, y + height/30))
        elif not game:
            restart_text = restart_font.render("Start", True, BLACK)
            screen.blit(restart_text, (x + width/30, y + height/30))


# Number of players
def number_of_players():
    if en:
        num_font = pygame.font.Font("Fonds/jack_font.TTF", 30)
    if cz:
        num_font = pygame.font.Font("Fonds/coolvetica.TTF", 30)
    num2_font = pygame.font.Font("Fonds/jack_font.TTF", 50)
    if en:
        num_text = num_font.render("Number of players", True, BLACK)
    elif cz:
        num_text = num_font.render("Počet hráčů", True, BLACK)
    num1_text = num2_font.render("1", True, WHITE)
    num2_text = num2_font.render("2", True, WHITE)
    x, y = (width//2) - ((num_text.get_width())//2), height / 8
    # Drawing rectangles
    pygame.draw.rect(screen, DARK_RED, (x-10, y + height/30-10, num_text.get_width()+20, num_text.get_height()+20))
    pygame.draw.rect(screen, BLACK, ((width//2) - 100, height/8 + height/7, 200, 50))
    if en:
        if players == 1:
            pygame.draw.rect(screen, VIOLET, (x+60, y + height/7, (num_text.get_width()-120)//2, num_text.get_height()+20))
        else:
            pygame.draw.rect(screen, VIOLET, (width//2, y + height/7, (num_text.get_width()-120)//2, num_text.get_height()+20))
    elif cz:
        if players == 1:
            pygame.draw.rect(screen, VIOLET, (width//2 - 80, height/8 + height/7, 80, 50))
        else:
            pygame.draw.rect(screen, VIOLET, (width//2, height/8 + height/7, 80, 50))
    # Drawing text
    screen.blit(num_text, (x, y + height/30))
    if en:
        screen.blit(num1_text, (x + width/6, y + height/7))
        screen.blit(num2_text, (x + 2*(width/6), y + height/7))
    elif cz:
        screen.blit(num1_text, (x-60 + width/6, y + height/7))
        screen.blit(num2_text, (x-60 + 2*(width/6), y + height/7))


# Close button
def close_button():
    mouse_pos = pygame.mouse.get_pos()
    x, y = width / 8 + 2*(width/8), height / 32 + 24*(height/32)
    if mouse_pos[0] > x and mouse_pos[0] < (width/8) + 4*(width/8) and mouse_pos[1] > y and mouse_pos[1] < y + (height/8):
        pygame.draw.rect(screen, DARK_RED, (x, y, 2*(width/8), height/8))
        close_font = pygame.font.Font("Fonds/jack_font.TTF", 30)
        close_text = close_font.render("Exit", True, BLACK)
        screen.blit(close_text, (x + width/16, y + height/30))
    else:
        pygame.draw.rect(screen, RED, (x, y, 2*(width/8), height/8))
        close_font = pygame.font.Font("Fonds/jack_font.TTF", 30)
        close_text = close_font.render("Exit", True, BLACK)
        screen.blit(close_text, (x + width/19, y + height/30))


# X
Xx1a, Xy1a = (width / 3) / 5, (height / 3) / 5
Xx1b, Xy1b = (width / 3) - (width / 3) / 5, (height / 3) - (height / 3) / 5
Xx2a, Xy2a = (width / 3) / 5, (height / 3) - (height / 3) / 5
Xx2b, Xy2b = (width / 3) - (width / 3) / 5, (height / 3) / 5


# fce X
def X():
    if pl_1 and pX_1:
        pygame.draw.line(screen, VIOLET, (Xx1a, Xy1a), (Xx1b, Xy1b), 20)
        pygame.draw.line(screen, VIOLET, (Xx2a, Xy2a), (Xx2b, Xy2b), 20)
    if pl_2 and pX_2:
        pygame.draw.line(screen, VIOLET, (Xx1a + width / 3, Xy1a), (Xx1b + width / 3, Xy1b), 20)
        pygame.draw.line(screen, VIOLET, (Xx2a + width / 3, Xy2a), (Xx2b + width / 3, Xy2b), 20)
    if pl_3 and pX_3:
        pygame.draw.line(screen, VIOLET, (Xx1a + 2*(width / 3), Xy1a), (Xx1b + 2*(width / 3), Xy1b), 20)
        pygame.draw.line(screen, VIOLET, (Xx2a + 2*(width / 3), Xy2a), (Xx2b + 2*(width / 3), Xy2b), 20)
    if pl_4 and pX_4:
        pygame.draw.line(screen, VIOLET, (Xx1a, Xy1a + height / 3), (Xx1b, Xy1b + height / 3), 20)
        pygame.draw.line(screen, VIOLET, (Xx2a, Xy2a + height / 3), (Xx2b, Xy2b + height / 3), 20)
    if pl_5 and pX_5:
        pygame.draw.line(screen, VIOLET, (Xx1a + width / 3, Xy1a + height / 3), (Xx1b + width / 3, Xy1b + height / 3), 20)
        pygame.draw.line(screen, VIOLET, (Xx2a + width / 3, Xy2a + height / 3), (Xx2b + width / 3, Xy2b + height / 3), 20)
    if pl_6 and pX_6:
        pygame.draw.line(screen, VIOLET, (Xx1a + 2*(width / 3), Xy1a + height / 3), (Xx1b + 2*(width / 3), Xy1b + height / 3), 20)
        pygame.draw.line(screen, VIOLET, (Xx2a + 2*(width / 3), Xy2a + height / 3), (Xx2b + 2*(width / 3), Xy2b + height / 3), 20)
    if pl_7 and pX_7:
        pygame.draw.line(screen, VIOLET, (Xx1a, Xy1a + 2*(height / 3)), (Xx1b, Xy1b + 2*(height / 3)), 20)
        pygame.draw.line(screen, VIOLET, (Xx2a, Xy2a + 2*(height / 3)), (Xx2b, Xy2b + 2*(height / 3)), 20)
    if pl_8 and pX_8:
        pygame.draw.line(screen, VIOLET, (Xx1a + width / 3, Xy1a + 2*(height / 3)), (Xx1b + width / 3, Xy1b + 2*(height / 3)), 20)
        pygame.draw.line(screen, VIOLET, (Xx2a + width / 3, Xy2a + 2*(height / 3)), (Xx2b + width / 3, Xy2b + 2*(height / 3)), 20)
    if pl_9 and pX_9:
        pygame.draw.line(screen, VIOLET, (Xx1a + 2*(width / 3), Xy1a + 2*(height / 3)), (Xx1b + 2*(width / 3), Xy1b + 2*(height / 3)), 20)
        pygame.draw.line(screen, VIOLET, (Xx2a + 2*(width / 3), Xy2a + 2*(height / 3)), (Xx2b + 2*(width / 3), Xy2b + 2*(height / 3)), 20)


# O
Ox, Oy = (width // 3)//2, (height // 3)//2


# fce O
def O():
    if pl_1 and pO_1:
        pygame.draw.circle(screen, RED, (Ox, Oy), (width // 3)//3, 10)
    if pl_2 and pO_2:
        pygame.draw.circle(screen, RED, (Ox + width // 3, Oy), (width // 3)//3, 10)
    if pl_3 and pO_3:
        pygame.draw.circle(screen, RED, (Ox + 2*(width // 3), Oy), (width // 3)//3, 10)
    if pl_4 and pO_4:
        pygame.draw.circle(screen, RED, (Ox, Oy + height // 3), (width // 3)//3, 10)
    if pl_5 and pO_5:
        pygame.draw.circle(screen, RED, (Ox + width // 3, Oy + height // 3), (width // 3)//3, 10)
    if pl_6 and pO_6:
        pygame.draw.circle(screen, RED, (Ox + 2*(width // 3), Oy + height // 3), (width // 3)//3, 10)
    if pl_7 and pO_7:
        pygame.draw.circle(screen, RED, (Ox, Oy + 2*(height // 3)), (width // 3)//3, 10)
    if pl_8 and pO_8:
        pygame.draw.circle(screen, RED, (Ox + width // 3, Oy + 2*(height // 3)), (width // 3)//3, 10)
    if pl_9 and pO_9:
        pygame.draw.circle(screen, RED, (Ox + 2*(width // 3), Oy + 2*(height // 3)), (width // 3)//3, 10)


# Symbol draw
def symbol_draw():
    X()
    O()


# Lines
def lines():
    pygame.draw.rect(screen, WHITE, (0, height / 3 - 2, width, 4))
    pygame.draw.rect(screen, WHITE, (0, height - (height / 3) - 2, width, 4))
    pygame.draw.rect(screen, WHITE, (width / 3 - 2, 0, 4, height))
    pygame.draw.rect(screen, WHITE, (width - (width / 3) - 2, 0, 4, height))


# Screen update
def renew_window():
    screen.fill(BLACK)
    lines()
    symbol_draw()
    if end:
        text_winner()
        number_of_players()
        restart_button()
        close_button()
        flags()
    if rule == -1:
        rules()
        flags()
    if not game:
        number_of_players()
        restart_button()
        close_button()
        flags()
    
    pygame.display.flip()


# Game loop / Restart
def game_loop():
    global running, FPS, clock, game, turn, pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7, pl_8, pl_9, pX_1, pX_2, pX_3, pX_4, pX_5, pX_6, pX_7, pX_8, pX_9, pO_1, pO_2, pO_3, pO_4, pO_5, pO_6, pO_7, pO_8, pO_9, m_1, m_2, m_3, m_4, m_5, m_6, m_7, m_8, m_9, rule, end, players
    running = True
    FPS = 60
    clock = pygame.time.Clock()
    turn = 1
    pl_1, pl_2, pl_3, pl_4, pl_5, pl_6, pl_7, pl_8, pl_9 = False, False, False, False, False, False, False, False, False
    pX_1, pX_2, pX_3, pX_4, pX_5, pX_6, pX_7, pX_8, pX_9 = True, True, True, True, True, True, True, True, True
    pO_1, pO_2, pO_3, pO_4, pO_5, pO_6, pO_7, pO_8, pO_9 = True, True, True, True, True, True, True, True, True
    m_1, m_2, m_3, m_4, m_5, m_6, m_7, m_8, m_9 = 1, 2, 3, 4, 5, 6, 7, 8, 9
    rule = 1
    end = False
    game = False

players = 1
game_loop()


while running:
    clock.tick(FPS)

    global rule
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Key and mouse assignments
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                # After clicking left mouse button
                if not end and rule == 1 and game:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pos = mouse_pos[0] // (width / 3), mouse_pos[1] // (height / 3)
                    # Player one
                    if turn == 1:
                        if mouse_pos == (0, 0) and m_1 == 1:
                            pO_1 = False
                            pl_1 = True
                            m_1 = "X"
                            turn = turn * -1
                        if mouse_pos == (1, 0) and m_2 == 2:
                            pO_2 = False
                            pl_2 = True
                            m_2 = "X"
                            turn = turn * -1
                        if mouse_pos == (2, 0) and m_3 == 3:
                            pO_3 = False
                            pl_3 = True
                            m_3 = "X"
                            turn = turn * -1
                        if mouse_pos == (0, 1) and m_4 == 4:
                            pO_4 = False
                            pl_4 = True
                            m_4 = "X"
                            turn = turn * -1
                        if mouse_pos == (1, 1) and m_5 == 5:
                            pO_5 = False
                            pl_5 = True
                            m_5 = "X"
                            turn = turn * -1
                        if mouse_pos == (2, 1) and m_6 == 6:
                            pO_6 = False
                            pl_6 = True
                            m_6 = "X"
                            turn = turn * -1
                        if mouse_pos == (0, 2) and m_7 == 7:
                            pO_7 = False
                            pl_7 = True
                            m_7 = "X"
                            turn = turn * -1
                        if mouse_pos == (1, 2) and m_8 == 8:
                            pO_8 = False
                            pl_8 = True
                            m_8 = "X"
                            turn = turn * -1
                        if mouse_pos == (2, 2) and m_9 == 9:
                            pO_9 = False
                            pl_9 = True
                            m_9 = "X"
                            turn = turn * -1
                    # Computer AI
                    if turn == -1 and players == 1 and (m_1 == 1 or m_2 == 2 or m_3 == 3 or m_4 == 4 or m_5 == 5 or m_6 == 6 or m_7 == 7 or m_8 == 8 or m_9 == 9):
                        comp = computer_move()
                        if comp == 1:
                            pX_1 = False
                            pl_1 = True
                            m_1 = "O"
                            turn = turn * -1
                        elif comp == 2:
                            pX_2 = False
                            pl_2 = True
                            m_2 = "O"
                            turn = turn * -1
                        elif comp == 3:
                            pX_3 = False
                            pl_3 = True
                            m_3 = "O"
                            turn = turn * -1
                        elif comp == 4:
                            pX_4 = False
                            pl_4 = True
                            m_4 = "O"
                            turn = turn * -1
                        elif comp == 5:
                            pX_5 = False
                            pl_5 = True
                            m_5 = "O"
                            turn = turn * -1
                        elif comp == 6:
                            pX_6 = False
                            pl_6 = True
                            m_6 = "O"
                            turn = turn * -1
                        elif comp == 7:
                            pX_7 = False
                            pl_7 = True
                            m_7 = "O"
                            turn = turn * -1
                        elif comp == 8:
                            pX_8 = False
                            pl_8 = True
                            m_8 = "O"
                            turn = turn * -1
                        elif comp == 9:
                            pX_9 = False
                            pl_9 = True
                            m_9 = "O"
                            turn = turn * -1

                    # Player two
                    elif turn == -1 and players == 2:
                        if mouse_pos == (0, 0) and m_1 == 1:
                            pX_1 = False
                            pl_1 = True
                            m_1 = "O"
                            turn = turn * -1
                        if mouse_pos == (1, 0) and m_2 == 2:
                            pX_2 = False
                            pl_2 = True
                            m_2 = "O"
                            turn = turn * -1
                        if mouse_pos == (2, 0) and m_3 == 3:
                            pX_3 = False
                            pl_3 = True
                            m_3 = "O"
                            turn = turn * -1
                        if mouse_pos == (0, 1) and m_4 == 4:
                            pX_4 = False
                            pl_4 = True
                            m_4 = "O"
                            turn = turn * -1
                        if mouse_pos == (1, 1) and m_5 == 5:
                            pX_5 = False
                            pl_5 = True
                            m_5 = "O"
                            turn = turn * -1
                        if mouse_pos == (2, 1) and m_6 == 6:
                            pX_6 = False
                            pl_6 = True
                            m_6 = "O"
                            turn = turn * -1
                        if mouse_pos == (0, 2) and m_7 == 7:
                            pX_7 = False
                            pl_7 = True
                            m_7 = "O"
                            turn = turn * -1
                        if mouse_pos == (1, 2) and m_8 == 8:
                            pX_8 = False
                            pl_8 = True
                            m_8 = "O"
                            turn = turn * -1
                        if mouse_pos == (2, 2) and m_9 == 9:
                            pX_9 = False
                            pl_9 = True
                            m_9 = "O"
                            turn = turn * -1

                # After clicking left mouse button in rule window or end window
                mouse_pos = pygame.mouse.get_pos()
                if rule == -1 or end or not game:
                    languages_fce(mouse_pos)
                # After clicking left mouse button
                if end or not game:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] > (width/8) + 2*(width/8) and mouse_pos[0] < (width/8) + 4*(width/8) and mouse_pos[1] > (height/8) + 4*(height/8) and mouse_pos[1] < (height/8) + 5*(height/8):
                        game_loop()
                        game = True
                    elif mouse_pos[0] > width / 8 + 2*(width/8) and mouse_pos[0] < (width/8) + 4*(width/8) and mouse_pos[1] > height / 32 + 24*(height/32) and mouse_pos[1] < height / 32 + 24*(height/32) + (height/8):
                        running = False
                    elif mouse_pos[0] > (width//2) - 80 and mouse_pos[0] < width//2 and mouse_pos[1] > height/8+height/7 and mouse_pos[1] < height/8+height/7 +60:
                        players = 1
                    elif mouse_pos[0] > width//2  and mouse_pos[0] < (width//2) + 80 and mouse_pos[1] > height/8+height/7 and mouse_pos[1] < height/8+height/7 +60:
                        players = 2
            # Before clicking right mouse button
            if pygame.mouse.get_pressed()[2] and rule == 1:
                if not end and game:
                    rule = -1
            elif pygame.mouse.get_pressed()[2] and rule == -1:
                rule = 1


    # Checking if game is not end
    the_end()

    # Renewing the window
    renew_window()

# Closing the game
pygame.quit()
