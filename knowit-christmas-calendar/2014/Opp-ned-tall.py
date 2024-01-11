__author__ = 'Vemund'


gyldigeTall = 0
for i in range(0,100001):
    tekstTall = str(i)
    liste = []
    for char in tekstTall:
        liste.append(char)
    liste.reverse()
    tekstTall = ""

    for nummer in liste:
        if nummer in ["2","3","4","5","7"]:
            tekstTall = tekstTall +"x"
        if nummer == "6":
            tekstTall = tekstTall +"9"
        elif nummer == "9":
            tekstTall = tekstTall +"6"
        else:
            tekstTall = tekstTall+nummer
    try:
        tekstTall = int(tekstTall)
        if i == tekstTall:
            gyldigeTall += 1
    except:
        pass
print(gyldigeTall)
