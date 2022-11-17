prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'Done' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'Done':
        print(f" {topping} is added to your pizza.")
    else:
        break