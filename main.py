from toemoji import spaceToEmoji
from configreader import Config


def readFromFile(filename:str) -> str:
    
    with open(filename) as file:
        res = file.read()
    
    return res

def writeToFile(filename:str, textToWrite:str) -> None:

    with open(filename, 'w+') as file:
        file.write(textToWrite)

config = Config()

SaveToFile = config.savetofile()
ReadFromFile = config.readfromfile()
ReadName =  config.readfilename()
SaveName = config.savefilename()
FileFormat = config.fileformat()

def main():
    
    if ReadFromFile:
        text = readFromFile(ReadName + FileFormat)
    else:
        text = input('>')

    res = spaceToEmoji(text)

    if SaveToFile:
        writeToFile(SaveName + FileFormat, res)
    else:
        return(res)


if __name__ == '__main__':
    main()