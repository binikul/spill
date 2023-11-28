import pygame
import random

class Figur():
    def __init__(self, bildesti: str,  skalering: float) -> None:
        self.før_bilde = pygame.image.load(bildesti).convert_alpha()
        self.bilde = pygame.transform.scale(self.før_bilde, (int(self.før_bilde.get_width() * skalering), int(self.før_bilde.get_height() * skalering)))
        self.rect = self.bilde.get_rect()
        
    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.bilde, self.rect)