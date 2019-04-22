# -- coding: utf-8 --
import csv


# 设置一些参数
# 数据文件存储名称
data_file = 'data.csv'
# 数据文件存储路径
path = r'../data/'


def create_csv(csv_head):
    with open(path + data_file, 'w', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(csv_head)


def append_csv(data):
    with open(path + data_file, "a+", newline='') as f:
        # 处理csv读写时不同换行符  linux:\n    windows:\r\n    mac:\r
        csv_file = csv.writer(f)
        csv_file.writerows(data)


def read_csv():
    csv_data = []
    with open(path + data_file) as f:
        csv_reader = csv.reader(f)  # 使用csv.reader读取f中的文件
        csv_header = next(csv_reader)  # 读取第一行每一列的标题
        csv_data.append(csv_header)
        for row in csv_reader:  # 将csv 文件中的数据保存到csv_data中
            csv_data.append(row)
    return csv_data
