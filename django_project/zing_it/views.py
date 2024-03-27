from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    music_types=['Pop','Rock','R&B','Soul & Funk','Blues','Reggae','Soundtracks','Dance & EDM','Rap', 'Asian Music','Jazz','Kpop','Metal','Electronic','Classical']
    return render(request,'zing_it/home.html',{"music_types":music_types})


def about(request):
    return HttpResponse("""通过 Zing，您可以轻松找到您想要的音乐并与其他人分享。您还可以浏览朋友、艺术家和名人的收藏，或创建自己的播放列表。
      使用 Zing 为您的生活配乐。免费订阅或收听。""")