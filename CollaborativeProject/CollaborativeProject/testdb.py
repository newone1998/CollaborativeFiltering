# -- coding: utf-8 --
from CollaborativeProject.CollaborativeModel.models import Song, User
from django.http import HttpResponse
from CollaborativeProject.data.Crawler import get_result
import uuid
import random
from django.core import serializers
from CollaborativeProject.preprocesing.preprocesing import main


def testdb(request):
    songs = get_result()
    for item in songs:
        song_form = format_to_song(item)
        songModel = Song(song_id=song_form[0], title=song_form[1], star=song_form[2],
                         singer=song_form[3], time=song_form[4], classification=song_form[5])
        songModel.save()
    return HttpResponse("<p>数据添加成功！</p>")


def create_user(request):
    for i in range(5):
        name = '用户' + str(i + 1)
        random_num = random.randint(0, 1)
        if random_num == 0:
            gender = True
        else:
            gender = False
        age = random.randint(18, 25)
        birth = str(2019-age) + '-' + str(random.randint(0, 11) + 1) + '-' + str(random.randint(0, 27) + 1)
        tag = '流行'
        user = User(name=name, gender=gender, age=age, birth=birth, tag=tag)
        user.save()
    return HttpResponse("<p>用户数据添加成功！</p>")


def song_pre(request):
    result_list = []
    song_list = Song.objects.all()
    for item in song_list:
        result_list.append(item.title)
    main(result_list)
    return HttpResponse("<p>歌曲数据添加成功！</p>")


def format_to_song(song):
    song_id = uuid.uuid1()
    title = song['title']
    star = song['star']
    brief_introduction = song['brief_introduction'].split(" / ")
    singer = brief_introduction[0]
    time = brief_introduction[1]
    if len(brief_introduction) > 4:
        classification = brief_introduction[4]
    else:
        classification = '暂无分类'
    return [str(song_id).replace('-', ''), title, star, singer, time, classification]
    # return HttpResponse(json.dumps([str(song_id).replace('-', ''), title, star, singer, time, classification]),
    #                     content_type="application/json")


def get_all_user(request):
    song_list = Song.objects.all()
    ajax_testvalue = serializers.serialize("json", song_list.order_by("-song_id")[:1])
    return HttpResponse(ajax_testvalue)
