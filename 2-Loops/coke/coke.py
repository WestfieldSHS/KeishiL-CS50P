coke_cost = 50
coins = [5, 10, 25]

while coke_cost > 0:
    print(f'COKE COST {coke_cost}.')
    inserted_coin = int(input("Insert coin: "))
    if inserted_coin in coins:
        coke_cost = coke_cost - inserted_coin
        print(f"Price remaining: {coke_cost}")

change = abs(coke_cost)
print(f'Change: {change}')