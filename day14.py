def sockMerchant(n, ar):
    colors = {}
    pairs = 0

    for sock in ar:
        if sock in colors:
            colors[sock] += 1
        else:
            colors[sock] = 1

    for count in colors.values():
        pairs += count // 2

    return pairs


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))

    print(sockMerchant(n, ar))