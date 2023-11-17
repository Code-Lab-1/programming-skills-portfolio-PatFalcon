McPattiBee_orders = ['BigPat', 'McPat grilled cheese', '5 kg Quarter McPatty', '12 Inch LongWilly McPats']
finished_McPattiBee = []

while McPattiBee_orders:
    current_McPattiBee = McPattiBee_orders.pop()
    print(f"I'm working on your {current_McPattiBee} sandwich. Please Wait.")
    finished_McPattiBee.append(current_McPattiBee)

print("\n")
for McPattiBee in finished_McPattiBee:
    print(f"I made a {McPattiBee} sandwich.")