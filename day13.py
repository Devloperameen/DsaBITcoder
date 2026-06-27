def catAndMouse(x, y, z):
    dist_a = abs(x - z)
    dist_b = abs(y - z)

    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        x, y, z = map(int, input().split())
        print(catAndMouse(x, y, z))