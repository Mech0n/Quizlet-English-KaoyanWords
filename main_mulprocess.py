import csv
import xlrd
from rich import print
from Iciba import Iciba
from concurrent.futures import ThreadPoolExecutor

# debug
import time

# 你Diy的单词本
InFilename = 'data.xls'
# 输出文本
OutFilename = 'eggs1.csv'

# 初始化Iciba模块
Dictionary = Iciba()
# Iciba 查词错误码
ErrIciba = -1

query_res = {}

def word(query):
    # eg: 
    #   query = "good"
    print('[bold yellow][INFO][/bold yellow] word() : Find \"%s\" .' % query.lower())
    word_query = Dictionary.get(query.lower())
    if word_query['errorCode'] is ErrIciba:
        return ErrIciba
    query_res[word_query["query"]] = word_query["value"]

def words():
    pool = ThreadPoolExecutor(20)
    for query in from_excel(InFilename):
        pool.submit(word, query)
    pool.shutdown(wait=True)
    

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

def to_csv(filename, words_res):
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile,
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)
        # eg:
        #   spamwriter.writerow(['Spam', 'assss'])
        #   spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        for key, value in words_res.items():
            spamwriter.writerow([key, value])


if __name__ == '__main__':
    start = time.time()
    words()
    to_csv(OutFilename, query_res)
    end = time.time()
    print('-' * 0x20)
    print('[bold yellow][INFO][/bold yellow] main() : Use time %s' % (end - start))
