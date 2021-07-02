import os
from tqdm import trange, tqdm
from data_read import JsonRead, textRead


class fudan_pro(object):
    def __init__(self, fudan_path):
        self.train_path = os.path.join(fudan_path, 'orig_data/train')
        self.test_path = os.path.join(fudan_path, 'orig_data/answer')

    def data_read(self, path, label2id, out_dataInfo):
        label_list = os.listdir(path)
        label_dict = label2id
        text_data = []
        if out_dataInfo:
            dataInfo = {'label2num': {}, 'textLen_info': []}
        for label_name in tqdm(label_list):
            label = label_dict[label_name]
            sub_text_path = os.path.join(path, label_name, 'utf8')
            text_sample_list = []
            sub_text_list = os.listdir(sub_text_path)
            if out_dataInfo:
                dataInfo['label2num'][label_name] = len(sub_text_list)
            for text_name in sub_text_list:
                text_sample = [label]
                text_dir = os.path.join(sub_text_path, text_name)
                text = textRead(text_dir)
                if out_dataInfo:
                    dataInfo['textLen_info'].append(len(text))
                text_sample.append(text)
                text_sample_list.append(text_sample)
            text_data.extend(text_sample_list)
        if out_dataInfo:
            return text_data, dataInfo
        else:
            return text_data

    def data_pro(self, label2id, out_dataInfo):
        train_data, train_info = self.data_read(self.train_path, label2id, out_dataInfo)
        test_data, test_info = self.data_read(self.test_path, label2id, out_dataInfo)
        return train_data, test_data, train_info, test_info

    def data_len_info(self, data_len):
        dataLen_info = {_: 0 for _ in range(10)}

        for num in data_len:
            index_key = num // 1000
            if index_key > 8:
                dataLen_info[9] += 1
            else:
                dataLen_info[index_key] += 1
        return dataLen_info


class insurance_pro(object):
    def __init__(self, insurance_path):
        self.insurance_train_path = os.path.join(insurance_path, 'iqa.train.tokenlized.pair.json')
        self.insurance_valid_path = os.path.join(insurance_path, 'iqa.valid.tokenlized.pair.json')
        self.insurance_test_path = os.path.join(insurance_path, 'iqa.test.tokenlized.pair.json')
        self.insurance_vocab_path = os.path.join(insurance_path, 'iqa.vocab.json')

    def dataRead(self):
        insurance_train_data = JsonRead(self.insurance_train_path)
        insurance_valid_data = JsonRead(self.insurance_valid_path)
        insurance_test_data = JsonRead(self.insurance_test_path)
        insurance_vocab_data = JsonRead(self.insurance_vocab_path)
        insurance_vocab_id2word = insurance_vocab_data['id2word']
        return insurance_train_data, insurance_valid_data, insurance_test_data, insurance_vocab_id2word

    def convert_ids_to_tokens(self, ids, id2word, is_out_text):
        text_tokens = []
        for token_id in ids:
            text_tokens.append(id2word[str(token_id)])
        if is_out_text:
            return ''.join(text_tokens)
        else:
            return text_tokens

    def sample_combine(self, insurance_data, id2word):
        new_insurance_data = []
        data_len = len(insurance_data)

        i = 0
        new_sample = {'qid': '', 'question': '', 'answers': [], 'label': []}
        while i < data_len:
            insurance_sample = insurance_data[i]
            insurance_sample_qid = insurance_sample['qid']
            if new_sample['qid'] == '':
                new_sample['qid'] = insurance_sample_qid
                new_sample['question'] = self.convert_ids_to_tokens(
                    insurance_sample['question'], id2word, True
                )
                new_sample['answers'].append(
                    self.convert_ids_to_tokens(insurance_sample['utterance'], id2word, True)
                )
                new_sample['label'].append(insurance_sample['label'][0])
            elif insurance_sample_qid == new_sample['qid']:
                if new_sample['question'] != self.convert_ids_to_tokens(
                        insurance_sample['question'], id2word, True
                ):
                    print(self.convert_ids_to_tokens(
                        insurance_sample['question'], id2word, True
                    ))
                if self.convert_ids_to_tokens(insurance_sample['utterance'], id2word, True) not in new_sample['answers']:
                    new_sample['answers'].append(
                        self.convert_ids_to_tokens(insurance_sample['utterance'], id2word, True)
                    )
                    new_sample['label'].append(insurance_sample['label'][0])
            else:
                assert len(new_sample['answers']) == len(new_sample['label'])
                new_insurance_data.append(new_sample)
                new_sample = {'qid': '', 'question': '', 'answers': [], 'label': []}
                new_sample['qid'] = insurance_sample['qid']
                new_sample['question'] = self.convert_ids_to_tokens(
                    insurance_sample['question'], id2word, True
                )
                new_sample['answers'].append(
                    self.convert_ids_to_tokens(insurance_sample['utterance'], id2word, True)
                )
                new_sample['label'].append(insurance_sample['label'][0])
            i += 1
        return new_insurance_data


def p(data, num=5):
    for i in range(num):
        print(data[i])


# insurance_path = os.path.join('F:\InsuranceQA', 'orig_data/pairs')
# pro = insurance_pro(insurance_path)
# insurance_train_data, insurance_valid_data, insurance_test_data, insurance_vocab_id2word = pro.dataRead()
# insurance_train_data = pro.sample_combine(insurance_train_data, insurance_vocab_id2word)
# insurance_valid_data = pro.sample_combine(insurance_valid_data, insurance_vocab_id2word)
# insurance_test_data = pro.sample_combine(insurance_test_data, insurance_vocab_id2word)


fudan_path = 'F:/NLPdata/FuDan'
label2id = {
    'C11-Space': 0, 'C15-Energy': 1, 'C16-Electronics': 2, 'C17-Communication': 3, 'C19-Computer': 4,
    'C23-Mine': 5, 'C29-Transport': 6, 'C3-Art': 7, 'C31-Enviornment': 8, 'C32-Agriculture': 9, 'C34-Economy': 10,
    'C35-Law': 11, 'C36-Medical': 12, 'C37-Military': 13, 'C38-Politics': 14, 'C39-Sports': 15, 'C4-Literature': 16,
    'C5-Education': 17, 'C6-Philosophy': 18, 'C7-History': 19
}
pro = fudan_pro(fudan_path)

a, b, c, d = pro.data_pro(label2id, True)

e = pro.data_len_info(c['textLen_info'])
f = pro.data_len_info(d['textLen_info'])
print(c['label2num'])
print(d['label2num'])