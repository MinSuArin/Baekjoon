n = int(input())
x = 1
while((x * x + x) / 2 < n):
    x += 1
if x % 2 == 1:
    sub = int((x * x + x) / 2 - n)
    grad_x = sub + 1
    grad_y = (x + 1) - grad_x
elif x % 2 == 0:
    sub = int((x * x + x) / 2 - n)
    grad_y = sub + 1
    grad_x = (x + 1) - grad_y

print("%d/%d"%(grad_x, grad_y))