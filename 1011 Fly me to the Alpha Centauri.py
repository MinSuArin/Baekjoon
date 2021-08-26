def count_move(dis):
    n = 1
    while pow(n, 2) + n < dis:
        n += 1
    if (dis <= pow(n, 2)):
        return (2 * n - 1)
    else:
        return (2 * n)
    
if __name__ == "__main__" :
    T = int(input())
    m_move = 0 # move ¼ö
    for i in range(T):
        x, y = map(int, input().split())
        distance = y - x
        m_move = count_move(distance)
        print(m_move)