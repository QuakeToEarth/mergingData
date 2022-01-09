import csv
dataset1 = []
dataset2 = []
finalPlanetData = []
with open('dataset_1.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

header1 = dataset1[0]
planetData1 = dataset1[1:]


with open('dataset_2_sorted.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

header2 = dataset2[0]
planetData2 = dataset2[1:]

finalHeaders = header1 + header2

for index, row in enumerate(planetData1):
    finalPlanetData.append(planetData1[index] + planetData2[index])


with open('merge.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(finalHeaders)
    csvwriter.writerows(finalPlanetData)
