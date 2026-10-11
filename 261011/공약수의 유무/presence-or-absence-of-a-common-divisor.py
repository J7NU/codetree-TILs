a,b = map(int, input().split())
result = 0
for i in range(a,b+1):
    if 1_920 % i == 0 and 2_880 % i == 0:
        result += 1
        break
if result > 0:
    print(1)
else:
    print(0)