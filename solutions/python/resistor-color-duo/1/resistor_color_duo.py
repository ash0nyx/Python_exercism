COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def value(colors):
    #create an empty string
    code = ''

    #take only the first two colors
    if len(colors) > 2:
        colors = colors[:2]

    #take the colors indexes and combine them as strings
    for color in colors:
            code += str(COLORS.index(color))

    #convert the result to an integer
    return int(code)