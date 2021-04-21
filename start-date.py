# find earliest year in each data set
# are months incremented or days
# move to next year if months, store date if days --> lable with ticker
# have all stored dates in file
# find earliest possible year
# crtl-k --> crtl-c for block comment
# crtl-k --> crtl-u for block un-comment

import csv

# find last earliest recorded year in csv file
with open('DATA/ZRX.csv', newline='') as csvfile:
    file = csvfile.readlines()
    length = len(file)
    for i in range((length-1), 0, -1):
        print(file[i])
        break

        # last_line = file[i]
        # year = int(last_line[6:10])
        # month1 = int(last_line[3:5])
        # next_line = file[i-1]
        # month2 = int(next_line[3:5])
        # if month2 - month1 == 0:
        #     earliest_date = last_line
        #     break
        # print(earliest_date)
        # elif month2 - month1 > 0:
        #     i = -2
        #     for i in range(length-1):
        #         last_line = file[i]
        #         next_line = file[i-1] 

