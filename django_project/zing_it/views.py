from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

music_types=[
            { "id": "1","name" : "Pop"}, { "id": "2","name" : "Rock"}, { "id": "3","name" : "R&B"}, { "id": "4","name" : "Soul & Funk"}, { "id": "5","name" : "Blues"}
    ]

biggest_hits_2018 = [
            {"id": 1, "Track": "告黑气球", "Artist": "周伦", "Album": "爱的第七章", "Length": "3:27"},
            {"id": 2, "Track": "大酒窝", "Artist": "蔡俊杰, 林卓妍", "Album": "JJ陆", "Length": "3:34"},
            {"id": 3, "Track": "Better Now", "Artist": "Post Malone", "Album": "beerbongs & bentleys", "Length": "3:51"},
            {"id": 4, "Track": "第一次", "Artist": "光优", "Album": "第一次个人创作专辑", "Length": "3:04"},
            {"id": 5, "Track": "冰雨", "Artist": "德华", "Album": "Pop", "Length": "3:21"},
            {"id": 6, "Track": "一起长大的约定", "Artist": "周伦", "Album": "我很忙", "Length": "3:14"},
        ]


def home(request):
    
    music_types=['Pop','Rock','R&B','Soul & Funk','Blues','Reggae','Soundtracks','Dance & EDM','Rap', 'Asian Music','Jazz','Kpop','Metal','Electronic','Classical']
    return render(request,'zing_it/home.html',{"music_types":music_types})


def about(request):
    return HttpResponse("""<h1>关于我们: </h1><p>通过 Zing，您可以轻松找到您想要的音乐并与其他人分享。您还可以浏览朋友、艺术家和名人的收藏，或创建自己的播放列表。
      使用 Zing 为您的生活配乐。免费订阅或收听。</p>""")

def music(request,id):
    # music_types=[
    #         { "id": "1","name" : "Pop"}, { "id": "2","name" : "Rock"}, { "id": "3","name" : "R&B"}, { "id": "4","name" : "Soul & Funk"}, { "id": "5","name" : "Blues"},
    #         { "id": "6","name" : "Reggae"}, { "id": "7","name" : "Soundtracks"}, { "id": "8","name" : "EDM"}, { "id": "9","name" : "Rap"}, { "id": "10","name" : "Asian Music"},
    #         { "id": "11","name" : "Jazz"}, { "id": "12","name" : "Kpop"}, { "id": "13","name" : "Metal"}, { "id": "14","name" : "Electronic"}, { "id": "15","name" : "Classical"},
    # ]
    print(id)
    for type in music_types:
        if type["id"] == id:
            return render(request,'zing_it/music_type.html',{"music": type,"songs":biggest_hits_2018})
    