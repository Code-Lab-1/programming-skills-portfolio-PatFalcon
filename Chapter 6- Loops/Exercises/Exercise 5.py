McPattiBee_orders = [
    'pastrami', '12 Inch LongWilly McPats', 'McPatty grilled cheese', 'pastrami',
    'McPatturkey', '6 Inch LongWilly McPats', 'pastrami']
finished_McPattiBee = []

print("Yeah, we're out of pastrami. You can order at McPats instead.")
while 'pastrami' in McPattiBee_orders:
    McPattiBee_orders.remove('pastrami')

print("\n")
while McPattiBee_orders:
    current_McPattiBee = McPattiBee_orders.pop()
    print(f"I'm working on your {current_McPattiBee} sandwich.")
    finished_McPattiBee.append(current_McPattiBee)

print("\n")
for McPattiBee in finished_McPattiBee:
    print(f"I made a {McPattiBee} sandwich.")