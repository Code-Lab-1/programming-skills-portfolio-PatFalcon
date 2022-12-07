guests = ['Stephanie', 'Mum', 'Nathan']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"\nSorry, {name} can't make it to dinner.")


del(guests[2])
guests.insert(1, 'Mark')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

#Print you can only invite 2 people
print(f"\nSorry, I can only invite two people.")
removed_element = guests.pop(1)
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
del(guests[0])
del(guests[1])
print(guests)
