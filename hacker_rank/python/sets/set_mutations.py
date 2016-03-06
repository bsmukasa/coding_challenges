"""Set Mutations

You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation
operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2∗N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

Output the sum of elements in set A.

"""
set_a = set(
    map(int, input().strip().split())
    if int(input().strip()) > 0
    else ''
)

for idx in range(int(input().strip())):
    method, set_length = tuple(input().strip().split())
    other_set = set(map(int, input().strip().split()))
    getattr(set_a, method)(other_set)

print(sum(set_a))