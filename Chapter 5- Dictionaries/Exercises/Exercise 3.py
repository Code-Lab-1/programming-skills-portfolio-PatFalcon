glossary = {
    'comment': 'Notes in a program.',
    'list': 'Specified order of collective items.',
    'loop': 'A collection of items, one at a time.',
    'string': 'Series of characters.',
    'value': 'Basically proper nouns in coding.',
    'key': 'The common noun in coding.',
    'conditional test': 'Comparison of one value to another.',
    'float': 'A numerical value with a decimal component.',
    'dictionary': "Pairs of keys with own respective values.",
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")