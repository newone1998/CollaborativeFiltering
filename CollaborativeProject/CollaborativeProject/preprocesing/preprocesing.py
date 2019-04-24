# -- coding: utf-8 --
import random
from CollaborativeProject.data.csv_handler import create_csv, append_csv

# 设置一些参数

# 歌曲数量
SONG_COUNT = 100
# 用户数量
USER_COUNT = 5
# 每首歌听过的最大次数
MAX_LICENSED_COUNT = 20


def get_index(count_temp):
    index_list_temp = []
    count = 0
    while count < count_temp:
        index = random.randint(1, USER_COUNT)
        if index != count_temp:
            count += 1
            index_list_temp.append(index)
    return index_list_temp


def get_all_users():
    csv_head = ['']
    for item in range(USER_COUNT):
        csv_head.append('用户' + str(item + 1))
    return csv_head


def get_all_songs():
    song_list = []
    for item in range(SONG_COUNT):
        song_list.append('song' + str(item + 1))
    return song_list


def main(song_list):
    create_csv(get_all_users())
    result_list = []
    # song_list = get_all_songs()
    for item in range(SONG_COUNT):
        listened_count = random.randint(0, USER_COUNT)
        result = [0 for _ in range(USER_COUNT + 1)]
        result[0] = song_list[item]
        if listened_count != 0:
            index_list = get_index(listened_count)
            for index in index_list:
                result[index] = random.randint(1, MAX_LICENSED_COUNT)
        result_list.append(result)
    print(result_list)
    append_csv(result_list)


if __name__ == '__main__':
    main()
