base_count, test_count = (tuple(map(int, input().strip().split())))
base = list(map(int, input().strip().split()))
improve, decline = (set(map(int, input().strip().split())) for _ in range(2))

feeling = sum([0 + 1 if num in improve else 0 - 1 if num in decline else 0 + 0 for num in base])

print(feeling)