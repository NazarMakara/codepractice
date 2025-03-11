sizes = {}
stack = []

txt = open("input_4.txt")
y = txt.readlines()

for line in y:
    part = line.strip().split()

    if part[0] == "$" and part[1] == "cd": # перехід в директорію
        if part[2] == "/":  # перехід до кореневої директорії
            stack = ["/"]  # Очищаємо стек і встановлюємо кореневу директорію
        elif part[2] == "..":  # перехід до батьківської директорії
            stack.pop()  # видаляємо останній елемент зі стека
        else:  
            stack.append(part[2])  # Додаємо ім'я директорії до стека

    elif part[0].isdigit(): 
        folder_size = int(part[0])  
        path = "/".join(stack)

        for i in range(len(stack)):
            parent_path = "/".join(stack[:i + 1])
            if parent_path not in sizes:
                sizes[parent_path] = 0
            sizes[parent_path] += folder_size

result = 0
for size in sizes.values():
    if size <= 100000:
        result += size

print(result)
