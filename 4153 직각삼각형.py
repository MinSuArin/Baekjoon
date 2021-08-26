if __name__ == "__main__" :
    a, b, c = map(int, input().split())
    while( a != 0) :
        max_num = max(a, b, c)
        min_num = min(a, b, c)
        cen_num = (a + b + c) - max_num - min_num
        if pow(max_num, 2) == pow(min_num, 2) + pow(cen_num, 2):
            print("right")
        else:
            print("wrong")
    
        a, b, c = map(int, input().split())