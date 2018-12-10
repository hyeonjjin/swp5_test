class Mylife:

    text = ["♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥","♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ","♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥","♥ ♥ ♥ ♥ ♥ ♥ ♥",
            "♥ ♥ ♥ ♥ ♥ ♥","♥ ♥ ♥ ♥ ♥","♥ ♥ ♥ ♥","♥ ♥ ♥","♥ ♥","♥"," "]
    def __init__(self):
        self.remainingLives = 0


    def getRemainingLives(self):
        return self.remainingLives


    def decreaseLife(self):
        self.remainingLives += 1


    def currentShape(self):
        return self.text[self.remainingLives]