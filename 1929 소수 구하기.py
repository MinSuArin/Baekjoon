if __name__ == "__main__" :
    m, n = map(int, input().split())
    is_break = 0
    for i in range(m, n + 1):
        if i == 1: continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_break = 1
                break
        if is_break == 1:
            is_break = 0
        else :
            print(i)

