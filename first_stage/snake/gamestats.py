
class Gamestats():
    def __init__(self, settings):
        self.gameActive = True

    def gameOver(self):
        self.gameActive = False