n = int(input())
sum = 0
cnt = 0
for i in range(n):
    num = int(input())
    sum += num
    cnt += 1

print(f"{sum} {sum/cnt:.1f}")