COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def label(colors):
    ohms = (COLORS.index(colors[0])*10 + COLORS.index(colors[1])) * (10 ** COLORS.index(colors[2]))
    
    if ohms >= 10 ** 9 :
        prefix = 'giga'
        ohms //= 10 ** 9
    elif ohms >= 10 ** 6 :
        prefix = 'mega'
        ohms //= 10 ** 6
    elif ohms >= 10 ** 3 :
        prefix = 'kilo'
        ohms //= 10 ** 3
    else :
        prefix = ''
    
    return f'{ohms} {prefix}ohms'