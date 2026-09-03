ls=list(input().split())
# print(len(ls))
sum=0
for i in range(len(ls)):
    # print(i)
    if i==2 or i == 4 or i == 9:
        sum+=int(ls[i])
print(sum)

