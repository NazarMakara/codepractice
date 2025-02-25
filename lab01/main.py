txt = open('input_1.txt')
y = txt.readlines()
right = []
left = []

for i in y:
    x = i.split()
    right.append(int(x[1]))
    left.append(int(x[0]))

def result(a, b):
    a.sort()
    b.sort()
    result_ = []
    for i in range(len(a)):
        res = abs(a[i] - b[i])
        result_.append(res)
    return sum(result_)

print(result(left, right))
