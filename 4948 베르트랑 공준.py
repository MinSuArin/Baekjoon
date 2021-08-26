if __name__ == "__main__" :
    
    is_prime = [False, False] + [True] * ((123456 * 2) - 1)
    primes = []
    for i in range(2, int((123456 * 2) + 1)):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, (123456 * 2) + 1, i):
                is_prime[j] = False
    num = int(input())
    while num != 0:
        m_cnt = 0
        for k in primes:
            if num < k <= num * 2:
                m_cnt += 1
            
        print(m_cnt)
        num = int(input())