a_m, a_e = map(int, input().split())
b_m, b_e = map(int, input().split())

if b_m > a_m:
    print("B")
elif a_m > b_m:
    print("A")
else:
    if b_e > a_e:
        print("B")
    else:
        print("A")
