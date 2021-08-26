def self_star(n):
    global board

    if n == 3:
        board[0][:3] = board[2][:3] = ["*"] * 3
        board[1][:3] = ["*"] + [" "] +["*"]
        return

    m = int(n // 3)
    self_star(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: continue
            for k in range(m):
                board[i * m + k][j * m: (j + 1) * m] = board[k][:m]
                
    return self_star(n/3)

if __name__ == "__main__" :
    N = int(input())
    board = [[" " for i in range(N)] for i in range(N)]
    self_star(N)
    m_str = ""
    for i in range(N):
        for j in range(N):
            m_str += board[j][i]
        m_str += '\n'
    
    print(m_str[:-1])