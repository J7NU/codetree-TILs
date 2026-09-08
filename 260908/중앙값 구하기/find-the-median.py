a,b,c = map(int, input().split())

mid = 0
if a >= b:
    if b >= c:
        mid = b
    else: # b < c
        if a >= c:
            mid = c
        else: # a < c
            mid = a
else: # a < b
    if c >= b:
        mid = b
    else: # c < b
        if a >= c:
            mid = a
        else: 
            mid = c

print(mid) 