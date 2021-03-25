import csv
import xlrd
from rich import print
from Iciba import Iciba

# debug 
import time

# 你Diy的单词本
InFilename = 'data.xls'
# 输出文本
OutFilename = 'eggs.csv'

Dictionary = Iciba()
ErrIciba = -1

def words():
    # 生成输出到csv的words :
    # eg :
    # {
    #   'asd' : 'n.asdsa',
    #   'ass' : 'n.asdsd'
    # }
    querys = from_excel(InFilename)

    res = {}
    for query in querys:
        print('[Info]Word function : Find %s .' % query.lower())
        word_query = Dictionary.get(query.lower())
        if word_query['errorCode'] is ErrIciba:
            continue
        res[word_query["query"]] = word_query["value"]
    
    return res


def from_excel(filename):
    # 读取生词本单词
    # eg:
    # |asd||
    # |abc||
    # 
    # return : ['asd', 'abc']
    excelfile = xlrd.open_workbook(filename)
    table = excelfile.sheets()[0]
    res = table.col_values(0)
    print(res)
    print('-' * 0x20)
    return res

def to_csv(filename, words):
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile,
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)
        # eg:
        #   spamwriter.writerow(['Spam', 'assss'])
        #   spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        for key, value in words.items():
            spamwriter.writerow([key, value])

if __name__ == '__main__':
    start = time.time()
    to_csv(OutFilename, words())
    end = time.time()
    print('-' * 0x20)
    print('[INFO] Use time %s' % (end - start))
