rep_num = int(input())
lst=[]
for i in range(rep_num):
    inp = input().split()
    
    if inp[0] == "push_front":
        lst.insert(0,int(inp[1]))
    
    elif inp[0] == "push_back":
        lst.append(int(inp[1]))
    
    elif inp[0] == "pop_front":
        print(lst[0])
        lst.pop(0)
    
    elif inp[0] == "pop_back":
        print(lst[-1])
        lst.pop()
    
    elif inp[0] == "size":    
        print(len(lst))
    
    elif inp[0] == "front":
        print(lst[0])
    
    elif inp[0] == "back":
        print(lst[-1])
    
    elif inp[0] =="empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)