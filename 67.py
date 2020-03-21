f = open("p067_triangle.txt", mode='r')
data = f.readlines()
f.close()
l = []
for k in data:
    l.append(list(map(int, k.split())))

for x in range(len(l) - 2, -1, -1):
    for k in range(len(l[x])):
        l[x][k] = max(l[x][k] + l[x + 1][k], l[x][k] + l[x + 1][k + 1])

print(l[0][0])
