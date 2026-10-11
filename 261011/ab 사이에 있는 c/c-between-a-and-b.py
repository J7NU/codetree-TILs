a,b,c = map(int, input().split())
res = 0
for i in range(a,b+1):
    if i % c == 0:
        res += 1
        break
if res == 1:
    print("YES")
else:
    print("NO")
