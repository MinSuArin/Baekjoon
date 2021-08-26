if __name__ == "__main__" :
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()
    m_cnt =  0
    is_break = 0
    for i in range(len(num)):
        if num[i] == 1: continue
        for j in range(2, int(num[i] / 2) + 1):
            if num[i] % j == 0:
                is_break = 1
                break
        if is_break == 1:
            is_break = 0
        else :
            m_cnt += 1
    print(m_cnt)