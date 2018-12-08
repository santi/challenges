__author__ = 'vemund'

with open('luke10', 'r') as f:
    data = map(float, f.readlines())
    intervall = -1
    for i in range(0, len(data), 1):
        inter1 = 0
        inter2 = 0
        for j in range(0, i, 1):
            min1 = data[j]
            for k in range(j, i, 1):
                maks1 = data[k]
                if inter1 < maks1 - min1:
                    inter1 = maks1 - min1
        for j in range(i, len(data), 1):
            min2 = data[j]
            for k in range(j, len(data), 1):
                maks2 = data[k]
                if inter2 < maks2 - min2:
                    inter2 = maks2 - min2
        if intervall < inter1 + inter2:
            intervall = inter1 + inter2
        print i, intervall
    print intervall



