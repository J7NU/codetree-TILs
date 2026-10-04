n = int(input())
start = 1

while n >= start:
    if start % 3 == 0:
        print(0,end=" ")
    elif start // 10 == 3 or start // 10 == 6 or start // 10 == 9:
        print(0,end=" ")
    elif start % 10 == 3 or start % 10 == 6 or start % 10 == 9:
        print(0,end=" ")
    else:
        print(start,end=" ")
    start += 1 
