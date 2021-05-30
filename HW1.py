print("Введите вашу хуйню")
a = ""
word = ""
#хуй хУй хуй жоПа жопа оПа опа ОПА
while a != "cancel":
    a = input()
    count = 1
    max = 1
    word = ""
    d = {}
    bigD = {}
    lst = list(a.lower().split(" "))
    for i in range(len(lst)):
        d.update({lst[i]: 0})
    for c in d:
        for i in range(len(lst)):
            if c == lst[i]:
                d[c] += 1
        if d[c] > max:
            max = d[c]
    for key, value in d.items():
        if value == max:
            print(f'{key} - {value}')
Z


        #print(lst)