import requests
import re
from bs4 import BeautifulSoup
from rich import print

class Iciba(object):

    def __init__(self):
        self.ErrIciba = -1
        super(Iciba, self).__init__()

    # 调用 iciba api 主体
    # source : https://github.com/caspartse/python-translate/blob/master/translate.py
    def query(self, word):
        sess = requests.Session()
        headers = {
            'Host': 'open.iciba.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate'
        }
        sess.headers.update(headers)
        url = 'http://open.iciba.com/huaci_new/dict.php?word=%s' % (word)
        try:
            resp = sess.get(url, timeout=100)
            text = resp.text
            pattern = r'(<div class=\\\"icIBahyI-group_pos\\\">[\s\S]+?</div>)'
            text = re.search(pattern, text).group(1)
        except:
            return None
        if (resp.status_code == 200) and (text):
            soup = BeautifulSoup(text, 'lxml')
            ps = soup.find_all('p')
            trans = []
            for item in ps:
                transText = item.get_text()
                transText = re.sub(
                    r'\s+', ' ', transText.replace('\t', '')).strip()
                if transText:
                    trans.append(transText)
            return ' '.join(trans)
        else:
            return None

    # 查词接口
    # 查询不到，返回 {'errorCode': -1, 'value': None}
    # 查询成功，返回 {'errorCode': 0, 'value': 释义}
    def get(self, word):
        res = {}
        response = self.query(word)
        if response is None:
            print("[bold red][ERROR][/bold red] Iciba.get() : Find \"%s\" Failed." % word)
            res["errorCode"] = self.ErrIciba
            res["query"] = word
            res["value"] = None
        else :
            print("[bold yellow][INFO][/bold yellow] Iciba.get() : Find \"%s\" ." % word)
            res["errorCode"] = 0
            res["query"] = word
            res["value"] = response
        return res

if __name__ == "__main__":
    # 测试
    a = Iciba()
    print(a.get("asdasda"))
    print(a.get("Oblige"))

'''

adj. 好的； 优秀的； 有益的； 漂亮的，健全的；
n. 好处，利益； 善良； 善行； 好人；
adv. 同well；

<class 'str'>
'''