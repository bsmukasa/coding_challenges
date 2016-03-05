""" No Idea!

There is an array of nn integers. There are also 22 disjoint sets, AA and BB, each containing mm integers. You like
all the integers in set AA and dislike all the integers in set BB. Your initial happiness is 00. For each ii integer
in the array, if i∈Ai∈A, you add 11 to your happiness. If i∈Bi∈B, you add −1−1 to your happiness. Otherwise,
your happiness does not change. Output your final happiness at the end.

"""
base_count, test_count = (tuple(map(int, input().strip().split())))
base = list(map(int, input().strip().split()))
improve, decline = (set(map(int, input().strip().split())) for _ in range(2))

feeling = sum([0 + 1 if num in improve else 0 - 1 if num in decline else 0 + 0 for num in base])

print(feeling)