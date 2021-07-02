import os
import json
import argparse


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


def p(data, num=5):
    for i in range(num):
        print(data[i])



