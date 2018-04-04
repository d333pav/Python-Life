import mylib

l = input().split()
n = int(l[0])
m = int(l[1])
k = int(l[2])
a = []
for i in range(n):
    a.append(list(input()))
mylib.life(n, m, k, a)

