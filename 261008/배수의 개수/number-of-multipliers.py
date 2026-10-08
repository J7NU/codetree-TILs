n3 = 0
n5 = 0 

for i in range(10):
    n = int(input())
    if n % 3 == 0:
        n3 += 1
    if n % 5 == 0:
        n5 += 1

print(n3,n5 )