if __name__ == "__main__" :
    
    is_prime = [False, False] + [True] * ((10000) - 1)
    primes = []
    for i in range(2, 10000 + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, 10000 + 1, i):
                is_prime[j] = False
    
    T = int(input())
    for i in range(T):
        num = int(input())
        for j in range(int(num / 2), 0, -1):
            if j in primes:
                if (num - j) in primes:
                    print("%d %d"%(j, num - j))
                    break