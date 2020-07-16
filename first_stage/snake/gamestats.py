class Gamestats():
    def __init__(self, settings):
        self.settings = settings
        self.gameActive = False

    def gameOver(self):
        self.gameActive = False

    def resetStats(self):
        self.gameActive = True
