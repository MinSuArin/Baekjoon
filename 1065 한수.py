n = int(input())
m_cnt = 0
m_tmp = 0
for i in range(1, n + 1):
    m_str = str(i)
    m_sub = 0
    if len(m_str) < 3:
        m_cnt += 1
    else:
        m_sub = int(m_str[0]) - int(m_str[1])
        for j in range(len(m_str) - 1):
            if int(m_str[j]) - int(m_str[j + 1]) != m_sub:
                m_tmp = 1
                break

        if m_tmp == 1:
            m_tmp = 0
        else:
            m_cnt += 1
print(m_cnt)

