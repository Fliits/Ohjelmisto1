syote2 = syote3 = 0
while True:
    syote1 = input("Anna luku: ")
    if syote1 == '':
        print(f"{syote2} {syote3}")
        break
    else:
        if syote2 == 0:
            syote2 = syote1
        if syote3 == 0:
            syote3 = syote1
        if syote1 < syote3:
            syote3 = syote1
        if syote1 > syote2:
            syote2 = syote1