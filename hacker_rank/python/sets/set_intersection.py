"""Set Intersection

The students of District College have subscriptions to English and French newspapers. Some students have subscribed
only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has
subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both
newspapers.

The first line contains nn, the number of students who have subscribed to the English newspaper.
The second line contains nn space separated roll numbers of those students.
The third line contains bb, the number of students who have subscribed to the French newspaper.
The fourth line contains bb space separated roll numbers of those students.

Output the total number of students who are subscribed to the English and French newspaper.

"""
english, french = (
    set(map(int, input().strip().split()))
    if int(input().strip()) > 0
    else set()
    for _ in range(2)
)

print(len(english & french))