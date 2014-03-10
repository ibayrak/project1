import csv
import sys

f = open('C:\some.csv', 'rt')
count=1
try:
    reader = csv.reader(f)
    next(f)
    for row in reader:
        print("Person %d" % count)
        print("First Name:"+row[0])
        print("Last Name:"+row[1])
        if row[2] != '':
            print("Email:"+row[2])
        if row[3] != '':
            print("Phone:"+row[3])
        print("")
        count +=1
finally:
    f.close()
