a = ""
while a != "cancel":
    end = 0
    a = input("Введите вашу хуйню\n")
    lst = set(a.split(" "))
    intlist = [int(x) for x in lst]
    intlist.sort()
    for i in range(len(intlist)):
        if intlist[i] != i + 1:
            print(i + 1)
            break
        if i == len(intlist) - 1:
            print(i+2)


