n, a = map(int, input().split())
start = 1
while start <= n :
    if start % a == 0:
        print(1)
    else:
        print(0)
    start += 1
