import os
import json
from tqdm import tqdm


def JsonRead(path):
    with open(path, encoding='utf-8', mode='r') as f:
        data = json.load(f)
    f.close()
    return data


def JsonReadOneEach(path):
    data = []
    with open(path, encoding='utf-8', mode='r') as f:
        for line in f:
            data.append(json.loads(line))
        f.close()
    return data


def textReadOneEach(path):
    data = []
    with open(path, encoding='utf-8', mode='r') as f:
        for line in f:
            data.append(line)
        f.close()
    return data


def textRead(path):
    text = open(path, encoding='utf-8').read()
    text = text.replace('\n', ' ').replace('\u3000', ' ')
    text = ' '.join(text.split())
    return text


def fileRead(path, label=None):
    file_name_list = os.listdir(path)
    text_list = []
    for file_name in tqdm(file_name_list):
        file_path = os.path.join(path, file_name)
        text = textRead(file_path)
        if label == None:
            text_list.append(text)
        else:
            text_list.append([text, label])
    return text_list


def p(data, num=5):
    for i in range(num):
        print(data[i])






