from random import randint

from configreader import Config


def spaceToEmoji(string:str) -> str:
    res = ''
    
    config = Config()

    file = open(f'{config.emojifile()}{config.fileformat()}')
    emojis = file.read().replace('\n', '').replace(' ', '')
    file.close()

    newstring = string.split('\n')
    string = ''
    for i in newstring:
        string += ' ' + i + ' \n'

    for i in range(len(string)):
        if string[i] != ' ':
            res += string[i]
        else:
            res += emojis[randint(0, len(emojis)-1)]
    
    return res

if __name__ == '__main__':
    ask = input('>')
    print(spaceToEmoji(ask))