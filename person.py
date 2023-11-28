from figur import Figur

class Person(Figur):
    def __init__(self, vindu_bredde: int, vindu_høyde: int) -> None:
        super().__init__("bilder/person.png", 0.4)
        self.liv = 10
        #setter spilleren i startposisjonen
        self.rect.centerx = vindu_bredde / 2
        self.rect.bottom = vindu_høyde

    def flytt(self, dx: int):
        self.rect.x += dx

    def kollisjon(self, eplex):
        return self.rect.colliderect(eplex)