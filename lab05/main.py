def game(file):
    limits = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    
    with open(file) as file:
        for line in file:
            id, rounds = line.split(": ")
            id = int(id.split()[1])

            rounds_list = [
                (int(num), color) 
                for round in rounds.split("; ") 
                for pair in round.split(", ") 
                for num, color in [pair.split()]
            ]
            if all(num <= limits[color] for num, color in rounds_list):
                total += id
    return total

print(game("input_5.txt"))