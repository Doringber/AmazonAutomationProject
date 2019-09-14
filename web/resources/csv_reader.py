import csv
list = []
with open('/Users/doringber/PycharmProjects/homework/amazon/web/resources/devices.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)
        list.append(row)

csvFile.close()

