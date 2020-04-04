class Core:
    __instance = None

    def __init__(self):
        pass

    @staticmethod
    def GetInstance(self):
        if self.__instance == None:
            self.__instance = Core()
        return self.__instance

    @classmethod
    def loop(self):
        print("core loop")
