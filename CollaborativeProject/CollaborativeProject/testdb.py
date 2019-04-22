from CollaborativeProject.CollaborativeModel.models import Song
from django.http import HttpResponse
from CollaborativeProject.data.Crawler import get_result
import uuid


def testdb(request):
    songs = get_result()
    for item in songs:
        song_form = format_to_song(item)
    songModel = Song(song_id='0123', title='fad', star=6.2, singer='qwe', time='222', classification='fadf')
    songModel.save()
    return HttpResponse("<p>数据添加成功！</p>")


def format_to_song(song):
    song_form_temp = []
    song_id = uuid.uuid1()
    title = song['title']
    star = song['star']
    brief_introduction = song['brief_introduction']
    return song_form_temp
