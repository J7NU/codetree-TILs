a,b = map(int,  input().split())

if a >= b:
    for i in range(b,a+1):
        if i % 2 == 1:
            print(i,end=" ")
        else:
            continue
else:
    for j in range(a,b+1):
        if j % 2 == 1:
            print(j,end=" ")