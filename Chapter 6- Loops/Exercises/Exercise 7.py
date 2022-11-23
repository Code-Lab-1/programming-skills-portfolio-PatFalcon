budget = 0
itemCost = 0
cartTotal = 0

on = "TRUE"

print("AYoO! Welcome to Al Hamid Jupaak!")
budget = float(input("How much are you willing to spend?"))
while on == "TRUE" :
    itemCost = input("How much is the recent item in your cart. Type DONE to quit. ")
    if itemCost == "DONE" :
        on = "FALSE"

    elif itemCost.isdigit() :
        cartTotal += float(itemCost)
        if cartTotal < budget :
            print("Ok, the items in your cart cost a total of ", cartTotal)
            print ("Your budget is ", budget, " you have spent ", cartTotal, " you have ", budget - cartTotal, " left over.")
        else :
            print("You are like the Philippine Government, broke. Please leave!")
            break
    else :
        print("Invalid entry!") #If neither a number nor ALL DONE was entered, this happens
        continue