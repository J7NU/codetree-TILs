a,b,c = map(int, input().split())
found = False
found = any(i % c == 0 for i in range(a,b+1))
if found == True:
    print("NO")
else:
    print("YES")