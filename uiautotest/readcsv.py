import csv
def readcsv(file):
    ls=[]
    with open(file,encoding='UTF-8') as f:
        text=csv.reader(f)
        for i in text:
            return i
# print(readcsv(file=r'D:\project\uiautotest\data.csv'))
