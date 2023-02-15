import csv
reader=csv.reaader(open('simplecsv'))
mydict={
}
for column in reader:
    mydict[column[0]] = {'age':column[1],'color':column[2]}
  
  
f=open("simplecsv")
ls=f.readlines()
data=ls.split(',')
print(data[0])

try:
    print(1/0)
except:
    print('Error')
else:
    print('Success')
finally:
    print('Done')








