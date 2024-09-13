print("Earned amount:")
print("""Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80""")
print()
result = 202 + 118 + 2250 + 1680 + 1075 + 80
print("Income: $" + str(result))


expense = input("Staff expenses:\n")
other_expenes = input("Other expenses:\n")
net_income = float(result) - float(expense) - float(other_expenes)
print("Net income: $" + str(int(net_income)))
