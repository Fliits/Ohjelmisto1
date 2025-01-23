tunnus = "python"
salasana = "rules"
toistot = 0
while toistot >= 4:
    ktunnus = input("Anna tunnus: ")
    ksalasana = input("Anna salasana: ")
    toistot = toistot + 1
    if ktunnus == tunnus and ksalasana == salasana:
        print("Tervetuloa!")
        break
    if ktunnus != tunnus or ksalasana != salasana:
        print("Pääsy evätty.")