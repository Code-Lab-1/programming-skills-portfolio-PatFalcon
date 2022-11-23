prompt = "\nEnter a song you want me to play"
prompt += "\nEnter 'Done' when you are done deciding: "

while True:
    song = input(prompt)
    if song != 'Done':
        print(f" {song} is added to queue. Do you want to add more?")
    else:
        break