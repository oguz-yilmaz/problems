def eggDrop(dropCount, floorCount):
    dropMax = 0

    floors = [0 for _ in range(dropCount + 1)]

    while floors[dropCount] < floorCount:
        for eggs in range(dropCount, 0, -1):
            floors[eggs] += 1 + floors[eggs - 1]
        dropMax += 1

    return dropMax


print(eggDrop(3, 100))
