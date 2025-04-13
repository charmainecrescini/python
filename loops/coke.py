# This file prompts the user to insert a coin, one at a time
# Each time informing the user of the amount due.

# Accepted denominations
denomination = [5, 10, 25]
# Coca-Cola (Coke) for 50 cents
amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}" )
    # Ask user to insert coin
    coin = int(input("Insert coin: "))
    if coin in denomination:
        amount_due -= coin
print(f"Change Owed: {abs(amount_due)}" )