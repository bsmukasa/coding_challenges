"""Check Strict Superset

You are given one set A and a number of other sets, N.
Your job is to find whether set A is a strict superset of all the N sets.
Print True, if A is a strict superset of all of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Input Format

The first line contains the space separated elements of set A.
The second line contains integer N, the number of other sets.
The next NN lines contains the space separated elements of the other sets.

Output Format

Print True if set AA is a strict superset of all other NN sets. Otherwise, print False.

"""
file = open('check_strict_superset_test.txt', 'r')
set_a = set(file.readline().strip().split())

results = [not bool(set(file.readline().strip().split()) - set_a) for _ in range(int(file.readline()))]

print(False not in results)