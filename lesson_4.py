def distinct_money(costs, money):
    distincts = {}
    for i, cost in enumerate(costs):
        diff = money - cost
        if diff in distincts:
            return i + 1, distincts[diff]
        distincts[cost] = i + 1

    return distincts.values()

trips = int(input("trips: "))

for _ in range(trips):
    money = int(input("money: "))
    flavours = int(input("number of flavours: "))
    costs = []
    for _ in range(flavours):
        costs.append(int(input("cost: ")))

    indices = distinct_money(costs, money)
    print(*indices)
