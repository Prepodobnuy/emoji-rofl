from random import randint


def spaceToEmoji(string:str) -> str:
    res = ''
    
    emoji_list = ['😀','🤢','🥺','🥹','😁','😆','😅','🙂','😚','😙','🤫','🤮','🤧','😎','🥸','😳','💀','😣','😈','👿','🤬','💔','❤️','🖤','🙈','😻','🤡','💩',]

    newstring = string.split('\n')
    string = ''
    for i in newstring:
        string += ' ' + i + ' \n'

    for i in range(len(string)):
        if string[i] != ' ':
            res += string[i]
        else:
            res += emoji_list[randint(0, len(emoji_list)-1)]
    
    return res

if __name__ == '__main__':
    ask = input('>')
    print(spaceToEmoji(ask))
    print(randint(1,10))