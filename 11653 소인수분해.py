if __name__ == "__main__" :
    n = int(input())
    if n != 1 :
        div_num = 2
        while div_num <= n:
            if n % div_num == 0:
                n = int(n / div_num)
                print(div_num)
            else:
                div_num += 1