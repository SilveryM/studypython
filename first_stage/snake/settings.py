class Settings():
    def __init__(self):
        self.screenWidth = 800
        self.screenHegiht = 600
        self.bgColor = (230, 230, 230)

        #方向枚举
        self.Direction = {'Left': 0, 'Up': 1, 'Right': 2, 'Down': 3}

        #难度(速度)
        self.speed = 1

        #sprite基本大小
        self.spriteSize = 10

        #游戏名称
        self.gameName = "Snake"