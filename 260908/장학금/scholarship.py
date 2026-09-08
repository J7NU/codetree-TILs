m,f = map(int, input().split())
if m >= 90 and f >=90:
    if f >= 95:
        print(100000)
    else:
        print(50000)
else:
    print(0)