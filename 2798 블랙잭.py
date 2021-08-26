if __name__ == "__main__" :
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    near_sum = a[0] + a[1] + a[2]
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if (M - (a[i] + a[j] + a[k]) < M - near_sum) and M - (a[i] + a[j] + a[k]) >= 0:
                    near_sum = a[i] + a[j] + a[k]

    print(near_sum)