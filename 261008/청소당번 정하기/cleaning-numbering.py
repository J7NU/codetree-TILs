n = int(input())

c_c = 0
h_c = 0
b_c =0 

for i in range(n,0,-1):
    if i % 12 == 0:
        b_c += 1
    elif i % 3 ==0:
        h_c += 1 
    elif i % 2 ==0:
        c_c += 1 

print(c_c,h_c,b_c)