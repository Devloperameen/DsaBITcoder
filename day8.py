k = int(input())
rooms = list(map(int, input().split()))

captain = (k * sum(set(rooms)) - sum(rooms)) // (k - 1)
print(captain)