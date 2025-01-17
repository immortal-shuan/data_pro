# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document
import os
import json
import requests
import random
import time
from hashlib import md5
from tqdm import trange


class baidutranslate(object):
    def __init__(self, from_lang, to_lang):
        self.appid = '20211206001020556'
        self.appkey = '6P8Eh13Ijvj_TV61KBlZ'
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        self.salt = random.randint(32768, 65536)
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def make_md5(self, s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    def gensign(self, query):
        sign = self.make_md5(self.appid + query + str(self.salt) + self.appkey)
        return sign

    def translate(self, querys):
        query = '\n'.join(querys)
        payload = {'appid': self.appid, 'q': query, 'from': self.from_lang, 'to': self.to_lang, 'salt': self.salt,
                       'sign': self.gensign(query)}
        # print(requests.post(self.url, params=payload, headers=self.headers).json())
        # time.sleep(1)
        trans_text = requests.post(self.url, params=payload, headers=self.headers).json()["trans_result"]

        result = {_['src']: _['dst'] for _ in trans_text}
        return result

    def back_translate(self, querys):
        result = self.translate(querys)
        time.sleep(1)
        temp_lang = self.from_lang
        self.from_lang = self.to_lang
        self.to_lang = temp_lang
        trans_texts = [_ for _ in result.values()]
        back_result = self.translate(trans_texts)
        out = {_:back_result[result[_]] for _ in result.keys()}
        return out


def OrigtextRead(path):
    data = []
    with open(path, encoding='utf-8', mode='r') as f:
        for line in f:
            sample = line.strip().split('\t')
            sample = [_.replace(' ', '') for _ in sample]
            assert len(sample) == 3
            data.append(sample)
        f.close()
    return data


def textsetRead(path):
    data = []
    with open(path, encoding='utf-8', mode='r') as f:
        for line in f:
            data.append(line.strip())
        f.close()
    return data


def SaveTxtSet(data, path):
    with open(path, mode='a', encoding='utf-8') as f:
        for sample in data:
            f.write(str(sample) + '\n')
        f.close()

def textSet(data):
    out = []
    for sample in data:
        out.append(sample[0])
        out.append(sample[1])
    return list(set(out))

# 因为存在不稳定的现象，所以我是每批次200数据处理完就存储
def backtranslatelist(data, med_lang):
    # 断掉的话，从哪断，就改0位置的数字为哪就行
    for i in trange(0, len(data), 200):
        temp_data = data[i:i+200]
        trans = baidutranslate('zh', med_lang)
        trans_text = trans.back_translate(temp_data)
        time.sleep(1)
        SaveToJson(trans_text, 'F:/data/NLPdata/LCQMC/txt_{}{}.json'.format(med_lang,i))
        print(i)


def SaveToJson(data, path):
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    f.close()

'''
因为元组每次的顺序都不一样，所以我先存储在读取，之后每次在处理200个数据
'''
# data_path = 'G:/similarity_match/data/train'
# data_type = ['BQ', 'LCQMC', 'OPPO']
# data_file = os.path.join(data_path, data_type[1], 'train')
# data = OrigtextRead(data_file)
# data_set = textSet(data)
# SaveTxtSet(data_set, 'F:/data/NLPdata/LCQMC/textset.txt')
data_set = textsetRead('F:/data/NLPdata/LCQMC/textset.txt')
backtranslatelist(data_set, 'en')
