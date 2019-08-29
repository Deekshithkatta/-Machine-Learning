import csv
general=[]
with open('dataset.csv','r') as csvfile:
    dataset = csv.reader(csvfile)
    for row in dataset:
        if 'yes' in row:
            general = row
            break

    for row in dataset:
        if 'yes' in row:
            for i in range(len(row)):
                if row[i]==general[i]:
                    pass
                else:
                    general[i]='?'
print(general[:-1])




