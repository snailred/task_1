n = int(input())
n_triangles = 0
num = 1
len = 0
for i in range(n):
    l = int(input())
    if len == l:
        num+=1
        if num==3:
            n_triangles+=1
            num = 0
    else:
        num = 1
        len = l
print(n_triangles)
