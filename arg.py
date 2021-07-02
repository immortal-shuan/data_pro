import argparse


def init_arg_parser():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--webqa_path', default='F:/NLPdata/WebQA.v1.0')
    arg_parser.add_argument('--insuranceqa', default='F:\InsuranceQA')
    args = arg_parser.parse_args()
    return args


