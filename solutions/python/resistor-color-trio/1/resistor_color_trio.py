COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def label(colors):
    answer = str(COLORS.index(colors[0])*10 + COLORS.index(colors[1]))
    if COLORS.index(colors[2]) == 9 :
        withz = str(answer + (COLORS.index(colors[2]) - 9) * '0' )
    if COLORS.index(colors[2]) >= 6 :
        withz = str(answer + (COLORS.index(colors[2]) - 6) * '0')
    if COLORS.index(colors[2]) >= 3 :
        withz = str(answer + (COLORS.index(colors[2]) - 3) * '0')
    withz = str(answer + (COLORS.index(colors[2])) * '0')

    if withz.count('0') == 9 :
        return str(int(int(withz) / 10 ** 9)) + ' gigaohms'
    if withz.count('0') >= 6 :
        return str(int(int(withz) / 10 ** 6)) + ' megaohms'
    if withz.count('0') >= 3 :
        return str(int(int(withz) / 10 ** 3)) + ' kiloohms'
    return withz + ' ohms'