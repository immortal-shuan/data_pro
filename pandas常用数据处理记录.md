# pandas常用数据处理记录

读取文件
```
data1 = pd.read_csv(data_path1)
```
数据信息
```
data1.info()
```
取出单独的一列
```
data_1 = data1.loc[:, [' Label']]
```
将其中一列数据的某些值映射成其他值
```
data['Label'] = data[' Label'].map({'BENIGN': 0, 'FTP-Patator': 1, 'SSH-Patator': 2})
```

