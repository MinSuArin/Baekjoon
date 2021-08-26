if __name__ == "__main__" :
    m = int(input())
    n = int(input())
    num = []
    m_cnt =  0
    is_break = 0
    for i in range(m, n + 1):
        if i == 1: continue
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                is_break = 1
                break
        if is_break == 1:
            is_break = 0
        else :
            num.append(i)

    if len(num) == 0:
        print(-1)
    else:
        print(sum(num))
        print(min(num))