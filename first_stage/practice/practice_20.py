#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

hei = 100
time = 10
tour = []
hegiht = []
for i in range(1, time):
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)

    hei /= 2
    hegiht.append(hei)

print('tour={0}'.format(sum(tour)))
print('height={0}'.format(hegiht[-1]))
