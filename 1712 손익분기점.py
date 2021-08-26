a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    benefit = c - b
    print((a // (c - b)) + 1)