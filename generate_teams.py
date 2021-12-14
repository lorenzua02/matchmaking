# Made by lorenzua02
# Discord: Lollo#9343
import json


def nextPossible(index=0):
    if index >= 10:
        return False

    if pointers[index]:
        pointers[index] = False
        return nextPossible(index + 1)
    else:
        pointers[index] = True
        if pointers.count(True) != 5:
            return nextPossible()
        return True


data = json.load(open('input.json'))
pointers, recordPointers = [], []
record = 99999  # TODO not clean, redo it

for i in range(10):
    pointers.append(False)

while nextPossible():
    mmr_a, mmr_b = 0, 0
    for i in range(10):
        if pointers[i]:
            mmr_a += data[i]["mmr"]
        else:
            mmr_b += data[i]["mmr"]
    diff = abs(mmr_a - mmr_b)
    if record > diff:
        record = diff
        recordPointers = pointers.copy()

players_a, players_b = [], []
for i in range(10):
    if recordPointers[i]:
        players_a.append(data[i]["name"])
    else:
        players_b.append(data[i]["name"])

print("Team A: ", players_a)
print("Team B: ", players_b)
# print("Difference: ", record)

input() # TODO another way to pause the program?

