import argparse


def init_data_path_arg():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--webqa_path', default='F:/NLPdata/WebQA.v1.0')
    arg_parser.add_argument('--insuranceqa', default='F:/InsuranceQA')

    args = arg_parser.parse_args()
    return args


def init_label2num_arg():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--ThucNews_label2num', default={
        '财经': 0, '彩票': 1, '房产': 2, '股票': 3, '家居': 4, '教育': 5, '科技': 6, '社会': 7,
        '时尚': 8, '时政': 9, '体育': 10, '星座': 11, '游戏': 12, '娱乐': 13
    })
    arg_parser.add_argument('--Fudan_label2num', default={
        'C11-Space': 0, 'C15-Energy': 1, 'C16-Electronics': 2, 'C17-Communication': 3, 'C19-Computer': 4,
        'C23-Mine': 5, 'C29-Transport': 6, 'C3-Art': 7, 'C31-Enviornment': 8, 'C32-Agriculture': 9, 'C34-Economy': 10,
        'C35-Law': 11, 'C36-Medical': 12, 'C37-Military': 13, 'C38-Politics': 14, 'C39-Sports': 15, 'C4-Literature': 16,
        'C5-Education': 17, 'C6-Philosophy': 18, 'C7-History': 19
    })

    args = arg_parser.parse_args()
    return args

