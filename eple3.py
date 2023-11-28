import random
from figur import Figur

class Eple3(Figur):
    def __init__(self, vindu_bredde: int) -> None:
        super().__init__("bilder/eple3.png", 0.1)
        self.verdi = -2
        # flytter ballen til startposisjonen
        self.hastighet = random.uniform(0.5, 2.0)
        self.rect.left = random.randint(0, vindu_bredde - self.rect.width)
        self.rect.top = 0
        self.ny_plassering(vindu_bredde)

    def fall(self, vindu_høyde: int):
        if self.rect.top > vindu_høyde:
            self.rect.y = 0
        self.rect.y += self.hastighet
        
    def ny_plassering(self, vindu_bredde: int):
        self.rect.centerx = random.randint(0, vindu_bredde)
        self.rect.top = 0