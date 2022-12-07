prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get free access! Enjoy the movie!")
    elif age < 13:
        print("  Your ticket price is 300 pesos.")
    else:
        print("  Your ticket price is 499 pesos.")