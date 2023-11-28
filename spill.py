from turtle import _Screen
import pygame
import random
from person import Person
from eple1 import Eple1
from eple2 import Eple2
from eple3 import Eple3
import high_score as high_score_module
from high_score import lagre_highscore

# 1. Oppsett
pygame.init()
BREDDE = 1000
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

spiller = Person(BREDDE, HOYDE)
epler = [Eple1(BREDDE), Eple2(BREDDE), Eple3(BREDDE)]

game_running = True

high_score_verdi = high_score_module.les_highscore()



bakgrunn = pygame.image.load("bilder/eplebakgrunn.jpeg").convert_alpha()
def tegn_bakgrunn():
    skalerbakgrunn = pygame.transform.scale(bakgrunn, (BREDDE, HOYDE))
    vindu.blit(skalerbakgrunn, (0,0))

font = pygame.font.SysFont("sans", 30)
poeng = 0

game_running = True


def poengfunksjon():
    poeng_text = font.render("Poeng: " + str(poeng), True, (255, 255, 255))
    vindu.blit(poeng_text, (10, 10))

    high_score_text = font.render("High Score: " + str(high_score_verdi), True, (255, 255, 255))
    vindu.blit(high_score_text, (10, 40))

    rødt_eple_text = font.render("Rødt eple = 1 poeng", True, (255, 0, 0))
    vindu.blit(rødt_eple_text, (BREDDE -325, 10))

    gull_eple_text = font.render("Gull eple = 2 poeng", True, (255, 215, 0))
    vindu.blit(gull_eple_text, (BREDDE -325, 40))

    rottent_eple_text = font.render("Rottent eple = -2 poeng", True, (128, 0, 0))
    vindu.blit(rottent_eple_text, (BREDDE -325, 70))




def restart_game():
    global game_running
    global poeng
    global high_score_verdi

    poeng = 0
    game_running = True



def display_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            restart_button = pygame.Rect(300, 200, 200, 50)
            quit_button = pygame.Rect(300, 300, 200, 50)

            pygame.draw.rect(vindu, (0, 255, 0), restart_button)
            pygame.draw.rect(vindu, (255, 0, 0), quit_button)

            restart_text = font.render("Restart", True, (0, 0, 0))
            quit_text = font.render("Quit", True, (0, 0, 0))

            vindu.blit(restart_text, (340, 210))
            vindu.blit(quit_text, (360, 310))

            if restart_button.collidepoint(mouse):
                if click[0] == 1:
                    restart_game()
                    return

            if quit_button.collidepoint(mouse):
                if click[0] == 1:
                    pygame.quit()
                    quit()

            pygame.display.update()



    
while game_running:
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            quit()

    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        spiller.flytt(-2)
    if taster[pygame.K_RIGHT]:
        spiller.flytt(2)

    if poeng > high_score_verdi:
        high_score_verdi = poeng
        high_score_module.lagre_highscore(high_score_verdi)


    # 3. Oppdater spill
    for eple in epler:
        eple.fall(HOYDE)

        if isinstance(eple, (Eple1, Eple2)) and eple.rect.top > HOYDE:
            poeng -= eple.verdi  # Trekk poeng for dette eplet
            eple.ny_plassering(BREDDE) 

        if spiller.kollisjon(eple.rect):
            if eple.rect.centery > spiller.rect.centery - 50: 
                poeng += eple.verdi
                eple.ny_plassering(HOYDE)


        if poeng < 0:
            game_running = False  # Sett spillets status til avsluttet
            display_menu()

    # 4. Tegn
    tegn_bakgrunn()
    poengfunksjon()
    spiller.tegn(vindu)
    for eple in epler:
        eple.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)


pygame.quit()
quit()