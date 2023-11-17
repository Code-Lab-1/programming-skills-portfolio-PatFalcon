prompt = "How much is your budget for college enrollment tuition fees?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    Budget = input(prompt)
    if Budget == 'quit':
        break
    Budget = float(Budget)

    if Budget > 50000:
        print("  You may enroll in Amnity University!")
    elif Budget < 50000:
        print("  You may enroll in BathSpa University.")
    else:
        print("  You are either broke or too rich to study.")