# find earliest year in each data set
# are months incremented or days
# move to next year if months, store date if days --> lable with ticker
# have all stored dates in file
# find earliest possible year
# crtl-k --> crtl-c for block comment
# crtl-k --> crtl-u for block un-comment

import csv

def yearSort(dates):
    return dates[6:10]

# find last earliest recorded year in csv file
print("These assets have a jump in at least one month recorded:")
with open('top_200.csv', newline='', encoding='utf-8-sig') as top200:
    file = csv.reader(top200, dialect='excel', delimiter=',', quotechar='|')
    earliest_dates = []
    for row in file:
        path1 = 'DATA/'
        path2 = row[0]
        path3 = '.csv'
        path = path1 + path2 + path3
        with open(path, newline='') as csvfile:
            file = csvfile.readlines()
            length = len(file)
            for i in range((length-1), 0, -1):
                date = file[i]
                month = int(date[3:5])
                date2 = file[i-1]
                month2 = int(date2[3:5])
                if (month2 - month) == 0:
                    earliest_dates.append(date[:10])
                    break
                else:
                    print(row[0])
earliest_dates.sort(key=yearSort)
file1 = open('earliest_dates.txt', 'w')
for item in earliest_dates:
    file1.writelines(item+'\n')
file1.close()
