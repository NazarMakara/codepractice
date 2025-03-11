file = 'input_2.txt'

def funcion(levels):
    up = True
    down = True
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if levels[i] >= levels[i + 1]: up = False
        if levels[i] <= levels[i + 1]: down = False
        if not (1 <= diff <= 3): 
            return False
    return up or down

def funcion2(file):
    with open(file) as file:
        safe_count = sum(funcion(list(map(int, line.split()))) for line in file)
    print(safe_count)

funcion2(file)
