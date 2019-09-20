def meeting_planner(slotsA, slotsB, dur):
    a, b = 0, 0
    while a < len(slotsA) and b < len(slotsB):
        if slotsA[a][1] < slotsB[b][0]:  # A is too early
            a += 1
        elif slotsA[a][0] > slotsB[b][1]:  # B is too early
            b += 1
        else:
            start = max(slotsA[a][0], slotsB[b][0])
            end = min(slotsA[a][1], slotsB[b][1])
            print(start, end)
            if end - start >= dur:
                return [start, start + dur]
            else:
                if slotsA[a][1] > slotsB[b][1]:
                    b += 1
                else:
                    a += 1
    return []  # if after going through all the slots, it doesn't return, then it fails

test3 = [[1,10]], [[2,3],[5,7]], 2
res = meeting_planner(test3[0], test3[1], test3[2])
print(res)




