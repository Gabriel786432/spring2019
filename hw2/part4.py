original = [[1, 2], [3, 4]]
new = []

for i in range(len(original)):
    to_add = []
    for j in range(len(original[0])):
        to_add.append(original[i][j])
        to_add.append(0)
    new.append(to_add)
    new.append([0 for i in range(len(original[0])*2)])

print(new)
