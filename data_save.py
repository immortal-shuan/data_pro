import json


def save_to_json(data, path):
    with open(path, encoding='utf-8', mode='a') as f:
        for line in data:
            pass


def product_save(data, path):
    with open(path, mode='a', encoding='utf-8') as f:
        for sample in data:
            f.write(str(sample) + '\n')
        f.close()

