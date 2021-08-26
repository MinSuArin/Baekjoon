import math

if __name__ == "__main__" :
    r = int(input())

    euclid_area = pow(r, 2) * math.pi
    taxi_area = pow(r * 2, 2) / 2

    print(euclid_area)
    print(taxi_area)