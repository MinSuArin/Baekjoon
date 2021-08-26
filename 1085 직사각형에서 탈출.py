if __name__ == "__main__" :
    x, y, w, h = map(int, input().split())
    if w - x <= x :
        dis_x = w - x
    else :
        dis_x = x

    if h - y <= y :
        dis_y = h - y
    else :
        dis_y = y

    if dis_x <= dis_y :
        print(dis_x)
    else:
        print(dis_y)