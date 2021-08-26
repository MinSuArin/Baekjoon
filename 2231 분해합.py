if __name__ == "__main__" :
    N = int(input())
    m_digits = len(str(N))
    aws = 0
    min = N - 9 * m_digits
    if min < 0 : min = 1
    for i in range(min, N):
        if i == N - sum([int(j) for j in str(i)]):
            aws = i
            break

    if aws == 0:
        print(0)
    else :
        print(aws)