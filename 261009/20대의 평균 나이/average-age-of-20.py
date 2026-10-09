sum,cnt  = 0,0

while True:
    n = int(input())
    if n // 10 != 2:
        print(f"{sum/cnt:.2f}")
        break
    sum += n
    cnt += 1
    