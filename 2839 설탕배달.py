n = int(input())
m_sum = 0
for i in range(n // 5, -1, -1):
    if (n - 5 * i) % 3 == 0:
        m_sum = i + ((n - 5 * i) // 3)
        break

if m_sum == 0:
    print(-1)
else:
    print(m_sum)