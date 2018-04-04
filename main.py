l = input().split()
n = int(l[0])
m = int(l[1])
k = int(l[2])
a = []
for i in range(n):
    a.append(list(input()))
for i in range(k):
    b = [['n'] * m for i in range(n)]
    for x in range(n):
        for y in range(m):
            if a[x][y] == 'r':
                b[x][y] = 'r'
            if a[x][y] == 'f' or a[x][y] == 's' or a[x][y] == 'n':
                neis = 0
                neif = 0
                for j1 in range(-1, 2):
                    for j2 in range(-1, 2):
                        if (j1 != 0 or j2 != 0) and (x+j1 > -1 and x+j1 < n and y+j2 > -1 and y+j2 < m):
                            if a[x+j1][y+j2] == 'f':
                                neif = neif + 1
                            elif a[x+j1][y+j2] == 's':
                                neis = neis + 1
                if a[x][y] == 's' and (neis == 2 or neis == 3):
                    b[x][y] = 's'
                if a[x][y] == 'f' and (neif == 2 or neif == 3):
                    b[x][y] = 'f'
                if a[x][y] == 'n' and neis == 3:
                    b[x][y] = 's'
                if a[x][y] == 'n' and neif == 3:
                    b[x][y] = 'f'
    a = b
for i in range(n):
    print(''.join(b[i]))
