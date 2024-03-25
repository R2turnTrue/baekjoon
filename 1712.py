jukja, prod_cost, cost = map(int, input().split())

if prod_cost >= cost:
    print(-1)
else:
    print(jukja // (cost - prod_cost) + 1)