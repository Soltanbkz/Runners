import random
import time

def shyrky_more_than_1():
    y = int(input("У скольки учасников развизались шнурки: "))
    shnyrky_sum = []
    for i in range(y):
        shnyrky = random.choice(list_runners)
        shnyrky_sum.append(shnyrky)
        index_shnyrky = list_runners.index(shnyrky)
        list_runners.insert(index_shnyrky + 3, shnyrky)
        list_runners.remove(shnyrky)
    print("Бегуны у которых развезались шнурки: ", *shnyrky_sum)
    print("Расположения бегунов в конце: ", *list_runners)

def runners():
    global runners
    global list_runners
    runners = int(input("Количество бегунов: "))
    list_runners = [int(i) for i in range(1, runners+1)]
    shnyrky = random.choice(list_runners)
    index_shnyrky = list_runners.index(shnyrky)
    list_runners.insert(index_shnyrky+3, shnyrky)
    print(f"Развизались шнурки у: {shnyrky}")
    list_runners.remove(shnyrky)
    print("Расположения бегунов в конце:", *list_runners)
    time.sleep(1)
    x = input("Хотите указать у скольки учасников развизались шнурки? \n")
    x = x.title()
    if x == "Да":
        shyrky_more_than_1()
    else:
        print("ОК")
runners()

input()