"""Set .discard()

You have a non-empty set ss, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.

The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s. All of the elements are non-negative integers,
less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Output the sum of the elements of set s after the commands have been executed.

"""
element_count = int(input().strip())
set_s = set(map(int, input().strip().split()))
for idx in range(int(input().strip())):
    row = input().strip().split()
    if row[0] == 'pop':
        getattr(set_s, row[0])()
    else:
        getattr(set_s, row[0])(int(row[1]))

print(sum(set_s))
