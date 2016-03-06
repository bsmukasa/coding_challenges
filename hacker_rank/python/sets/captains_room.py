"""Captain's Room

One fine day, a finite number of tourists come to stay at the hotel with infinite rooms.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K members per group where K ≠ 11.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of
the tourists. The room numbers will appear K times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.

Input Format
The first line consists of an integer, K, the size of each group.
The second line contains the unordered elements of the room number list.

Output the Captain's room number.

"""
group_size, room_numbers = int(input()), list(map(int, input().strip().split()))
captain = (sum(set(room_numbers)) * group_size - sum(room_numbers)) // (group_size - 1)
print(captain)