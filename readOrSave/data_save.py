import json


def SaveToJson(data, path):
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    f.close()


def SaveToJsonOneEach(data, path):
    with open(path, mode="a", encoding='utf-8') as f:
        for dict in data:
            f.write(json.dumps(dict, ensure_ascii=False))
            f.write('\n')
        f.close()


def SaveToTxt(data, path):
    with open(path, mode='a', encoding='utf-8') as f:
        for sample in data:
            f.write(str(sample) + '\n')
        f.close()




