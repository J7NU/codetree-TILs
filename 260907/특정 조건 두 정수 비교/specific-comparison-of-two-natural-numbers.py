a,b = map(int, input().split())
res_1 =0
res_2 =0

if a < b:
    res_1 =1
    
else:
    res_1 =0

if a == b:
    res_2 =1
    
else:
    res_2 =0



print(res_1,res_2)