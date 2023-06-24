class Config():
    def __init__(self, name:str='config'):
        self.name = name

    def GetConfig(self) -> list:
        
        with open(self.name) as config:
            return config.read().split('\n')

    def savetofile(self) -> bool:

        if self.GetConfig()[0].split(' ')[1] == '1':
            return True
        return False

    def readfromfile(self) -> bool:

        if self.GetConfig()[1].split(' ')[1] == '1':
            return True
        return False

    def savefilename(self) -> str:
        return self.GetConfig()[2].split(' ')[1]

    def readfilename(self) -> str:
        return self.GetConfig()[3].split(' ')[1]

    def emojifile(self) -> str:
        return self.GetConfig()[4].split(' ')[1]

    def fileformat(self) -> str:
        return self.GetConfig()[5].split(' ')[1]