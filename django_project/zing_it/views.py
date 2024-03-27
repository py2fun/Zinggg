from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .forms import Signup,Login, Edit

from .models import Song, Playlist

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

    new_playlist= Playlist.objects.all()
    return render(request,'zing_it/home.html',{"my_playlists":new_playlist})


def about(request):
    thankyou_next= Song.objects.create(track="告黑气球",artist="周伦",album="爱的第七章",length="3:27",playlist_id=1)
    one_kiss_next= Song.objects.create(track="大酒窝",artist="蔡俊杰, 林卓妍",album="JJ陆",length="3:34",playlist_id=1)
    better_now= Song.objects.create(track="Better Now",artist="Post malone",album="beerbongs & bentleys",length="3:51",playlist_id=1)
    the_middle= Song.objects.create(track="第一次",artist="光优",album="第一次个人创作专辑",length="3:04",playlist_id=1)
    love_lies= Song.objects.create(track="冰雨",artist="德华",album="Pop",length="3:21",playlist_id=2)
    rise= Song.objects.create(track="一起长大的约定",artist="周伦",album="我很忙",length="3:14",playlist_id=2)

    car_playlist= Playlist.objects.create(name="Car Playlist",number_of_songs=4)
    coding_playlist= Playlist.objects.create(name="Coding Playlist",number_of_songs=2)

    try:
        thankyou_next.save()
        one_kiss_next.save()
        better_now.save()
        the_middle.save()
        love_lies.save()
        rise.save()
        car_playlist.save()
        coding_playlist.save()
    except Exception as e: 
        print(e)

def playlist(request,id):
    songs=[]
    playlist_name=''

    new_playlist= Playlist.objects.all()

    for playlist in new_playlist:
        if(id == playlist.id):
            playlist_name=playlist.name

    if len(playlist_name)==0:
        raise Http404("Such playlist does not exist")

    new_songs= Song.objects.all()

    print(new_songs)


    for song in new_songs:
        if(id == song.playlist_id):
            songs.append(song)
        
    return render(request,'zing_it/songs.html',{"songs":songs,"playlist_name": playlist_name})

def edit(request,id):
    form = Edit(request.POST or None)
    if form.is_valid():
        track= form.cleaned_data.get("track")
        album = form.cleaned_data.get("album")
        artist = form.cleaned_data.get("artist")
        length = form.cleaned_data.get("length")
        playlist_id = form.cleaned_data.get("playlist_id")

        song= Song.objects.get(id=id)

        song.track= track
        song.album = album
        song.artist = artist
        song.length = length
        song.playlist_id = playlist_id

        song.save()

        return render(request,'zing_it/edit.html',{"form":form,"status": "Your song is updated successfully!" })

    return render(request,'zing_it/edit.html',{"form":form})

def signup(request):
    form = Signup(request.POST or None)
    if form.is_valid():
        password= form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        if(password!= confirm_password):
            return render(request,'zing_it/signup.html',{"form":form,"status":"Your passwords don't match!"})
        else:
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
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            status="You have successfully logged in!"
        else:
            status="You credentials are not valid. Try again!"
    return render(request,'zing_it/login.html',{"form":form,"status":status})

    