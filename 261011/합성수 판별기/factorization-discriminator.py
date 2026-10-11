n = int(input())
res = 0
for i in range(2,n):
    if n % i == 0:
        res += 1
        break
    else:
        continue
if res > 0:
    print("C")
else:
    print("N")