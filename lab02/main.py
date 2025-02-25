file = open('../lab02/input_2.txt', 'r')
lines = file.readlines()

def is_safe(lst):
    direction = lst[0] > lst[1]
    safe = 1 

    for i in range(len(lst) - 1):
        diff = lst[i] - lst[i + 1]

        if direction:
            if lst[i] <= lst[i + 1] or diff >= 4:
                safe = 0
                break
        else:
            if lst[i] >= lst[i + 1] or diff <= -4:
                safe = 0
                break

    return safe

res = 0
for line in lines:
    numbers = list(map(int, line.split()))
    if is_safe(numbers):
        res += 1

print(res)
