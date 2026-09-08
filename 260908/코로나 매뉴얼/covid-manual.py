a1,b1 = input().split()
a2,b2 = input().split()
a3,b3 = input().split()

A=B=C=D = 0
dct = {"cold": [a1,a2,a3], "temp":[int(b1),int(b2),int(b3)]}
# dct["temp"] = map(int, dct["temp"])
# print(dct["temp"])
result = []
for i in range(len(dct["cold"])):
    # print(i)
    if dct["cold"][i] == "Y":
        if dct["temp"][i] >= 37:
            A += 1
        else:
            C += 1
    else:
        if dct["temp"][i] >= 37:
            B += 1
        else:
            D += 1
if A >= 2:
    print("E")
else:
    print("N")
        