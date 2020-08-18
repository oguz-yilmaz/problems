

def getMaxValue(carrotTypes, capacity):
    MAX_WEIGHT = capacity
    NUM_ITEMS = len(carrotTypes)

    memo = [
        [0 for j in range(MAX_WEIGHT+1)]
        for i in range(NUM_ITEMS+1)
    ]

    for i in range(NUM_ITEMS):
        val = carrotTypes[i]["price"]
        wt = carrotTypes[i]["kg"]

        for j in range(MAX_WEIGHT+1):
            if carrotTypes[i]["kg"] > j:
                memo[i+1][j] = memo[i][j]
            else:
                biggestPossibleWeight = j - wt
                if biggestPossibleWeight < 0:
                    biggestPossibleWeight = 0

                switchOff = memo[i][j]
                switchOn = memo[i][biggestPossibleWeight] + val
                memo[i+1][j] = max((switchOff, switchOn))

    return memo[NUM_ITEMS][capacity]


carrotTypes = [{"kg": 5, "price": 100}, {
    "kg": 7, "price": 150}, {"kg": 3, "price": 70}]
print(getMaxValue(carrotTypes, 6))
