"""Set .add()

The first line contains an integer N, the total number of country stamps.
The next N lines contains the countrey's name where the stamp is from.
Find the total number of distinct country stamps.

"""
stamps = set(input().strip() for _ in range(int(input().strip())))
print(len(stamps))