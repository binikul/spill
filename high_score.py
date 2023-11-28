import os


def lagre_highscore(high_score):
    with open("highscore.txt", "w") as file:
        file.write(str(high_score))

def les_highscore():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            return int(file.read())
    else:
        return 0