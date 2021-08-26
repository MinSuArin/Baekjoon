def hanoi(K, a, b, c):
    if K == 1:
        print(a, c)
        return
    
    hanoi(K - 1, a, c, b)
    print(a, c)
    hanoi(K - 1, b, a, c)

if __name__ == "__main__" :
    K = int(input())
    print(pow(2, K) - 1)
    hanoi(K, 1, 2, 3)
