Guitar_orders = ['FlyingV', 'Thunderbird', 'Stratocaster', 'Jazzmaster']
finished_Guitar_orders= []

while Guitar_orders:
    current_orders = Guitar_orders.pop()
    print(f"I'm working on your {current_orders} sandwich. Please Wait.")
    finished_Guitar_orders.append(current_orders)

print("\n")
for Guitar_orders in finished_Guitar_orders:
    print(f"I made a {Guitar_orders} sandwich.")