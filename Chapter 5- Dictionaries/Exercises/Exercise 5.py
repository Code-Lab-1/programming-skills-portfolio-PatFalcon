# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'Cat',
    'name': 'Pipa',
    'owner': 'Mario',
    'weight': 44,
    'eats': 'Humans',
}
pets.append(pet)

pet = {
    'animal type': 'Tiger',
    'name': 'Rudolph',
    'owner': 'Mark',
    'weight': 80,
    'eats': 'Butter Chicken',
}
pets.append(pet)

pet = {
    'animal type': 'Dog',
    'name': 'Riley',
    'owner': 'Pats',
    'weight': 77,
    'eats': 'Toe nails',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")