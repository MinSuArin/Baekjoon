if __name__ == "__main__" :
    N = int(input())
    person = []
    ranking = ""

    for i in range(N) :
        person.append(list(map(int, input().split())))
    for j in range(len(person)) :
        m_rank = 1
        for k in range(len(person)) :
            if j == k : continue
            if person[j][0] < person[k][0] and person[j][1] < person[k][1] :
                m_rank += 1
        ranking = ranking + str(m_rank) + " "

    print(ranking[:-1])