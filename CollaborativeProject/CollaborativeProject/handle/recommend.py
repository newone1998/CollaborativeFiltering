# -- coding: utf-8 --
from CollaborativeProject.handle.data_class import DataClass


# 设置参数
# 推荐歌曲数量
RECOMMEND_COUNT = 10


def main():
    # data_class = DataClass()
    # print(data_class.all_users)
    # print(data_class.all_data)
    # print(data_class.get_row_by_song('song1'))
    # print(data_class.get_col_by_user('user1'))
    # print(data_class.get_fancy_degree_by_user_and_song('user1', 'song1'))
    # print(data_class.get_similarity_by_two_songs('song1', 'song2'))
    # print(data_class.get_listened_song_list_by_user('user1'))
    print(get_recommend_list('用户1'))
    pass


def get_recommend_list(user):
    recommend_list = []
    song_similarity_list = []
    fancy_degree_list = []
    data_class = DataClass()
    song_list = data_class.get_listened_song_list_by_user(user)
    for item in song_list:
        fancy_degree = data_class.get_fancy_degree_by_user_and_song(user, item)
        fancy_degree_list.append(fancy_degree)
    song_not_list = data_class.get_not_listened_song_list_by_user(user)
    similarity_list = [0 for _ in range(len(song_not_list))]
    for i in range(len(song_not_list)):
        for j in range(len(song_list)):
            fancy_degree = fancy_degree_list[j]
            similarity = data_class.get_similarity_by_two_songs(song_not_list[i], song_list[j])
            similarity_list[i] = similarity_list[i] + similarity * fancy_degree
    for item in range(len(song_not_list)):
        song_tuple = (song_not_list[item], similarity_list[item])
        song_similarity_list.append(song_tuple)
    song_similarity_list.sort(key=lambda song: song[1], reverse=False)
    if len(song_similarity_list) >= RECOMMEND_COUNT:
        song_similarity_list = song_similarity_list[0:10]
    for item in song_similarity_list:
        recommend_list.append(item[0])
    return recommend_list


if __name__ == '__main__':
    main()
