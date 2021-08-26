t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    num = [x for x in range(1, n + 1)]
    for __ in range(k):
        for j in range(1, n):
            num[j] += num[j-1]
    print(num[-1])