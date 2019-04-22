# -- coding: utf-8 --
from CollaborativeProject.data.csv_handler import read_csv
import numpy
import numpy as np


# 设置参数
np.seterr(divide='ignore', invalid='ignore')


class DataClass:
    all_users = []
    all_data = []

    def get_fancy_degree_by_user_and_song(self, user, song):
        user_col = self.get_col_by_user(user)
        song_col = self.get_col_by_user('')
        song_index = song_col.index(song)
        song_count = user_col[song_index]
        return self.mean_by_list(user_col, song_count)

    def get_similarity_by_two_songs(self, song1, song2):
        song_col = self.get_col_by_user('')
        song_index1 = song_col.index(song1)
        song_index2 = song_col.index(song2)
        song_matrix1 = self.all_data[song_index1]
        song_matrix2 = self.all_data[song_index2]
        song_matrix1 = song_matrix1[1:]
        song_matrix1 = map(int, song_matrix1)
        song_matrix2 = song_matrix2[1:]
        song_matrix2 = map(int, song_matrix2)
        return numpy.corrcoef(list(song_matrix1), list(song_matrix2))[0, 1]

    def get_listened_song_list_by_user(self, user):
        song_list = []
        song_col = self.get_col_by_user('')
        user_col = self.get_col_by_user(user)
        for item in range(len(user_col)):
            if int(user_col[item]) != 0:
                song_list.append(song_col[item])
        return song_list

    def get_not_listened_song_list_by_user(self, user):
        song_list = []
        song_col = self.get_col_by_user('')
        user_col = self.get_col_by_user(user)
        for item in range(len(user_col)):
            if int(user_col[item]) == 0:
                song_list.append(song_col[item])
        return song_list

    def get_row_by_song(self, song):
        for item in self.all_data:
            if song == item[0]:
                return item

    def get_col_by_user(self, user):
        index = 0
        col_data = []
        for item in self.all_users:
            if item == user:
                index = self.all_users.index(item)
                break
        for item in self.all_data:
            col_data.append(item[index])
        return col_data

    @staticmethod
    def mean_by_list(data_list, data):
        sum_count = 0
        for item in data_list:
            item_int = int(item)
            sum_count += item_int
        return int(data) / sum_count

    def __init__(self):
        result = read_csv()
        self.all_users = result[0]
        self.all_data = result[1:]
