from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User

from .forms import Signup,Login

# Create your views here.

music_types=[
            { "id": "1","name" : "Pop"}, { "id": "2","name" : "Rock"}, { "id": "3","name" : "R&B"}, { "id": "4","name" : "Soul & Funk"}, { "id": "5","name" : "Blues"}
    ]

my_songs = [
            {"id": 1, "Track": "告黑气球", "Artist": "周伦", "Album": "爱的第七章", "Length": "3:27","playlist_id": 1},
            {"id": 2, "Track": "大酒窝", "Artist": "蔡俊杰, 林卓妍", "Album": "JJ陆", "Length": "3:34","playlist_id": 1},
            {"id": 3, "Track": "Better Now", "Artist": "Post Malone", "Album": "beerbongs & bentleys", "Length": "3:51","playlist_id": 1},
            {"id": 4, "Track": "第一次", "Artist": "光优", "Album": "第一次个人创作专辑", "Length": "3:04","playlist_id": 1},
            {"id": 5, "Track": "冰雨", "Artist": "德华", "Album": "Pop", "Length": "3:21","playlist_id": 2},
            {"id": 6, "Track": "一起长大的约定", "Artist": "周伦", "Album": "我很忙", "Length": "3:14","playlist_id": 2},
        ]

my_playlists=[
    {"id":1,"name":"Car Playlist","numberOfSongs":4},
    {"id":2,"name":"Coding Playlist","numberOfSongs":2}
]

users = [
            {"id": 1, "full_name": "john", "email": "john123@gmail.com", "password": "adminpass"},
        ]

def home(request):
    
    music_types=['Pop','Rock','R&B','Soul & Funk','Blues','Reggae','Soundtracks','Dance & EDM','Rap', 'Asian Music','Jazz','Kpop','Metal','Electronic','Classical']
    return render(request,'zing_it/home.html',{"music_types":my_playlists})


def about(request):
    return HttpResponse("""<h1>关于我们: </h1><p>通过 Zing，您可以轻松找到您想要的音乐并与其他人分享。您还可以浏览朋友、艺术家和名人的收藏，或创建自己的播放列表。
      使用 Zing 为您的生活配乐。免费订阅或收听。</p>""")

def playlist(request,id):
    songs=[]
    playlist_name=''
    for playlist in my_playlists:
        if(id == playlist['id']):
            playlist_name=playlist['name']

    if len(playlist_name)==0:
        raise Http404("Such playlist does not exist")

    for song in my_songs:
        if(id == song['playlist_id']):
            songs.append(song)
        
    return render(request,'zing_it/songs.html',{"songs":songs,"playlist_name": playlist_name})

def signup(request):
    form = Signup(request.POST or None)
    if form.is_valid():
        password= form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        print(email)
        if(password!= confirm_password):
            return render(request,'zing_it/signup.html',{"form":form,"status":"Your passwords don't match!"})
        else:
            print("this is:",email)
            try:
                user= User.objects.get(email=email)
                return render(request,'zing_it/signup.html',{"form":form,"status":"This email already exists in the system! Please log in instead."})
            except Exception as e:
                print(e)
                new_user = User.objects.create_user(username= name, email= email,password= password)
                new_user.save()
                return render(request,'zing_it/signup.html',{"form":form,"status":"Signed up Successfully!"})
    return render(request,'zing_it/signup.html',{"form":form})
    
def login(request):
    form = Login(request.POST or None)
    status= " "
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = next((user for user in users if user["email"] == email and user["password"] == password), None)
        if user:
            status="Successfully logged in!"
        else:
            status="Wrong Credentials!"
    return render(request,'zing_it/login.html',{"form":form,"status":status})

    