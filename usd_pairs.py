import csv

def usd_pairs ():
    with open("bit-pairs.txt", newline='') as pairs:
        file = csv.reader(pairs, dialect='excel', delimiter=',', quotechar='|')
        USDCount = 0
        USDList = []
        for asset in file:
            pairList = asset
        for i in range(len(pairList)):
            if 'USD' in pairList[i]:
                USDCount += 1
                USDList.append(pairList[i].strip('\"'))
    file1 = open('usd_pairs.txt', 'w+')
    for item in USDList:
        file1.writelines(item+'\n')
    file1.close()
    return USDList

usd_pairs()