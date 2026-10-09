n = int(input())

lst = []
for i in range(1, n ):
    if n % i == 0:
        lst.append(i)
# print(lst)
# print(sum(lst))
if sum(lst) == n:
    print("P")
else:
    print("N")