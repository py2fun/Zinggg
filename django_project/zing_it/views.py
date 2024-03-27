from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    biggest_hits_2018 = [
            {"id": 1, "Track": "告黑气球", "Artist": "周伦", "Album": "爱的第七章", "Length": "3:27"},
            {"id": 2, "Track": "大酒窝", "Artist": "蔡俊杰, 林卓妍", "Album": "JJ陆", "Length": "3:34"},
            {"id": 3, "Track": "Better Now", "Artist": "Post Malone", "Album": "beerbongs & bentleys", "Length": "3:51"},
            {"id": 4, "Track": "第一次", "Artist": "光优", "Album": "第一次个人创作专辑", "Length": "3:04"},
            {"id": 5, "Track": "冰雨", "Artist": "德华", "Album": "Pop", "Length": "3:21"},
            {"id": 6, "Track": "一起长大的约定", "Artist": "周伦", "Album": "我很忙", "Length": "3:14"},
        ]
    return render(request,'zing_it/home.html',{"songs": biggest_hits_2018})


def about(request):
    return HttpResponse("""通过 Zing，您可以轻松找到您想要的音乐并与其他人分享。您还可以浏览朋友、艺术家和名人的收藏，或创建自己的播放列表。
      使用 Zing 为您的生活配乐。免费订阅或收听。""")