import os
import jionlp as jio
from tqdm import trange, tqdm


'''
同音替换
替换时，优先使用常用词汇（依据词频而定）
augmentation_num: 返回几条增强后的数据,默认3
homo_ratio:参数控制对每一个汉字的调整其位置概率
allow_mispronounce:是否允许方言读音误读，如 zh 与 z 卷舌不分，默认为 True，允许词汇错音
res = jio.homophone_substitution(text, augmentation_num=3, allow_mispronounce=True)
'''
def homophone_replace(texts):
    res = {}
    for text in tqdm(texts):
        homophone_text = jio.homophone_substitution(text)
        res[text] = homophone_text
    return res


'''
同音替换
替换时，优先使用常用词汇（依据词频而定）
augmentation_num:参数控制返回几条增强后的数据
add_ratio:对每一个位置随机增加字符概率，默认为 0.02
delete_ratio:对每一个汉字随机做删除的概率，默认为 0.02
res = jio.random_add_delete(text, augmentation_num=3)
'''
def randomadddelete(texts):
    res = {}
    for text in tqdm(texts):
        adddelete_text = jio.random_add_delete(text)
        res[text] = adddelete_text
    return res
