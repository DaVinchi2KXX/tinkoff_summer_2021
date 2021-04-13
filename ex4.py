data = list(map(int, input().split(' ')))
parcels = []
for i in range(data[0]):
    parcels.append(int(input()))
counter = 0
boxes = list()
box = list()
price = 0
for parcel in parcels:
    if data[0] - 1 > counter:
        if parcel - parcels[counter - 1] > 1:
            price += (max(box) - min(box)) * (len(box) * len(box)) + data[2]
            box.clear()
            box.append(parcel)
        elif parcel > parcels[counter + 1]:
            if parcel - parcels[counter + 1] > 1:
                price += (max(box) - min(box)) * (len(box) * len(box)) + data[2]
                box.clear()
                box.append(parcel)
                price += (max(box) - min(box)) * (len(box) * len(box)) + data[2]
                box.clear()
            else:
                box.append(parcel)
        elif parcel - parcels[counter - 1] < -1 and counter > 0 and parcel != 1 and box:
            price += (max(box) - min(box)) * (len(box) * len(box)) + data[2]
            box.clear()
            box.append(parcel)
        else:
            box.append(parcel)
    else:
        if parcels[counter-1]-parcel==1:
            box.append(parcel)
        else:
            box.clear()
            box.append(parcel)
            price += (max(box) - min(box)) * (len(box) * len(box)) + data[2]
        price += (max(box) - min(box)) * (len(box) * len(box)) + data[2]
    counter += 1

print(price)
