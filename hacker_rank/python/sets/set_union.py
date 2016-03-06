"""Set Union

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is
subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of
students who have subscribed to at least one newspaper.

The first line contains an integer, nn, the number of students who have subscribed to the English newspaper.
The second line contains nn space separated roll numbers of those students.
The third line contains bb, the number of students who have subscribed to the French newspaper.
The fourth line contains bb space separated roll numbers of those students.

Output the total number of students who are subscribed to the English or French newspaper.

"""
english, french = (
    set(map(int, input().strip().split()))
    if int(input().strip()) > 0
    else set()
    for _ in range(2)
)

print(len(english | french))
