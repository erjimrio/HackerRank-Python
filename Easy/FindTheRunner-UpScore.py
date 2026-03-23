if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))
    new_arr = []

    maximus = max(arr)

    for i in arr:
        if i < maximus:
            new_arr.append(i)

    print(max(new_arr))





