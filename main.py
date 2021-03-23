import csv
import xlrd
from rich import print
from Iciba import Iciba

# 你Diy的单词本
InFilename = 'data.xls'
# 输出文本
OutFilename = 'eggs.csv'

Dictionary = Iciba()
ErrIciba = -1

def words():
    # 生成输出到csv的words :
    # eg :
    # [
    #   ['asd', 'n.asdsa']
    #   ['asd', 'n.asdsd']
    # ]
    querys = from_excel(InFilename)

    res = []
    for query in querys:
        print('[Info]Word function : Find %s .' % query.lower())
        word_query = Dictionary.get(query.lower())
        if word_query['errorCode'] is ErrIciba:
            continue
        word_res = []
        word_res.append(word_query["query"])
        word_res.append(word_query["value"])
        res.append(word_res)
    
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
        for word in words:
            spamwriter.writerow(word)

if __name__ == '__main__':
    to_csv(OutFilename, words())
