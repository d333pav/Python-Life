def life(n=0, m=0, k=0, a=[]):
    for i in range(k):
        b = [['n'] * m for i in range(n)]
        for x in range(n):
            for y in range(m):
                if a[x][y] == 'r':
                    b[x][y] = 'r'
                else:
                    dict = {
                        's': 0,
                        'f': 0
                    }
                    for j1 in range(-1, 2):
                        for j2 in range(-1, 2):
                            if (j1 != 0 or j2 != 0) and (x + j1 > -1 and x + j1 < n and y + j2 > -1 and y + j2 < m):
                                if a[x + j1][y + j2] != 'n' and a[x + j1][y + j2] != 'r':
                                    dict[a[x + j1][y + j2]] += 1
                                    '''
                for s in dict:
                    if a[x][y] == s and (dict[s] == 2 or dict[s] == 3):
                        b[x][y] = s
                    if a[x][y] == 'n' and dict[s] == 3:
                        b[x][y] = s
                '''
                if a[x][y] == 's' and (dict['s'] == 2 or dict['s'] == 3):
                    b[x][y] = 's'
                if a[x][y] == 'f' and (dict['f'] == 2 or dict['f'] == 3):
                    b[x][y] = 'f'
                if a[x][y] == 'n' and dict['s'] == 3:
                    b[x][y] = 's'
                if a[x][y] == 'n' and dict['f'] == 3:
                    b[x][y] = 'f'

        a = b
    for i in range(n):
        print(''.join(b[i]))
