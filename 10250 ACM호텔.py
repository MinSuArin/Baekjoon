n = int(input())

for i in range(n):
    h, w, ord = map(int, input().split())
    if ord % h == 0 : m_h = h
    else : m_h = ord % h
    if ord / h == ord // h:
        m_w = ord // h
    else :
        m_w = (ord // h) + 1
    room = (m_h * 100) + m_w
    print(room)