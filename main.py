from toemoji import spaceToEmoji


def readconf() -> bool:
    
    SaveToText = False
    ReadFromFile = True
    SaveName = 'result.txt'
    ReadName = 'text.txt'

    with open('config') as file:
        conf_list = file.read().split('\n')
        
        if conf_list[0].split()[1] == '1':
            SaveToText = True
        
        if conf_list[1].split()[1] == '0':
            ReadFromFile = False

        SaveName = conf_list[2].split()[1]
        ReadName = conf_list[3].split()[1]
    
    return SaveToText, ReadFromFile, ReadName, SaveName

def readFromFile(filename:str) -> str:
    
    with open(filename) as file:
        res = file.read()
    
    return res

def writeToFile(filename:str, text:str) -> None:

    with open(filename, 'w+') as file:
        file.write(text)

SaveToText, ReadFromFile, ReadName, SaveName = readconf()

def main():
    
    if ReadFromFile:
        text = readFromFile(ReadName)
    else:
        text = input('>')

    res = spaceToEmoji(text)

    if SaveToText:
        writeToFile(SaveName, res)
    else:
        print(res)


if __name__ == '__main__':
    main()