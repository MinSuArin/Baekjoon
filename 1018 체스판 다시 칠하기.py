def cal_cnt(board):
    cnt_w = 0
    cnt_b = 0
    
    for i in range(8):
        for j in range(8):
            #if board[0][0] == w
            if ((i + j) % 2 == 1 and board[i][j] == "W"):
                cnt_w += 1
            elif ((i + j) % 2 == 0 and board[i][j] == "B"):
                cnt_w += 1
            #if board[0][0] == w
            if ((i + j) % 2 == 0 and board[i][j] == "W"):
                cnt_b += 1
            elif ((i + j) % 2 == 1 and board[i][j] == "B"):
                cnt_b += 1
    return max(cnt_w, cnt_b)

if __name__ == "__main__" :
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        board.append([ch for ch in input()])
    aws = 8 * 8

    for i in range(N - 7):
        for j in range(M - 7):
            slice_board = [one_row[j:j+8] for one_row in board[i:i+8]]
            cnt = cal_cnt(slice_board)
            aws = min(cnt, aws)

    print(aws)