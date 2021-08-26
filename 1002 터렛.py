import math

if __name__ == "__main__" :
    T = int(input())

    for i in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        if distance == 0 and r1 == r2:
            print(-1)
        elif distance == 0:
            print(0)
        elif r1 + r2 < distance or distance < abs(r1 - r2):
            print(0)
        elif r1 + r2 == distance or distance == abs(r1 - r2):
            print(1)
        else:
            print(2)