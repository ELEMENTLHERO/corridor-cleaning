# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy
import itertools
import random

def tryRemove(_list,element):
    try:
        _list.remove(element)
    except:
        pass

def groupsProg():
    combos = []
    people = ["Alex","Zhou","Linus","Lukas","Nicole","Gustav","Albin","Jaad"]
    allreadyChosen = []
    allreadyCombos = [] #those who have cleaned together already

    for p1 in people:
        if len(allreadyChosen) == len(people):
            break
        while(True):
            p2 = random.choice(people)
            if p1 in allreadyChosen:
                break
            if p1 == p2:
                continue
            if {p1, p2} in combos:
                continue
            if p1 in allreadyChosen or p2 in allreadyChosen:
                continue
            combos.append({p1, p2})
            allreadyChosen.append(p1)
            allreadyChosen.append(p2)
            break

    #tryRemove(combos,{"Josefin","Zhou"})
    tryRemove(combos,{"Linus","Lukas"})
    tryRemove(combos,{"Nicole","Gustav"})
    tryRemove(combos,{"Albin","Jaad"})

    #tryRemove(combos, {"Josefin", "Linus"})
    tryRemove(combos, {"Gustav", "Lukas"})
    tryRemove(combos, {"Jaad", "Zhou"})
    tryRemove(combos, {"Albin", "Nicole"})

    tryRemove(combos, {"Zhou", "Lukas"})
    tryRemove(combos, {"Nicole", "Linus"})
    tryRemove(combos, {"Jaad", "Gustav"})
    #tryRemove(combos, {"Albin", "Josefin"})

    tryRemove(combos, {"Lukas", "Linus"})
    tryRemove(combos, {"Gustav", "Jaad"})
    #tryRemove(combos, {"Nicole", "Josefin"})
    tryRemove(combos, {"Albin", "Zhou"})

    return combos



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    groups = groupsProg()
    while len(groups) < 4:
        groups = groupsProg()

    print("Non shuffled (Josefin first)",groups)
    random.shuffle(groups)
    print("Shuffled list: ",groups)
