from django.urls import path
from zing_it import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about/',views.about,name="about"),
    path('music/<id>',views.music,name="music"),
]