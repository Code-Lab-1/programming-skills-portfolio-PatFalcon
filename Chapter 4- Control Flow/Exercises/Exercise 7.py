How_many_hours_do_you_play_Valorant = int(input())

if How_many_hours_do_you_play_Valorant < 2:
    print("You're barely a player!")
elif How_many_hours_do_you_play_Valorant < 4:
    print("You're probably a player!")
elif How_many_hours_do_you_play_Valorant < 13:
    print("You're a member of Cloud 9?")
elif How_many_hours_do_you_play_Valorant < 20:
    print("Do you even have a life?")
elif How_many_hours_do_you_play_Valorant < 65:
    print("You're probably dead")
else:
    print("You definately are dead.")