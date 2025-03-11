def score(opponent, your):
    move = {'X': 1, 'Y': 2, 'Z': 3}
    outcomes = {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3
    }
    return move[your] + outcomes[(opponent, your)]

def total_score(file):
    score_ = 0
    with open(file) as file:
        for line in file:
            opponent, your = line.strip().split(' ')
            score_ += score(opponent, your)
    
    return score_

print(total_score("input_6.txt"))
