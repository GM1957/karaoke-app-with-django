from django.shortcuts import render, HttpResponse
from . models import Song,tempSong
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
import os
from django.conf import settings
from django.views.static import serve 

import ffmpeg
# Create your views here.
def home(request):
    allsongs = Song.objects.all()
    contex = {'allsongs': allsongs}
    return render(request, 'home/home.html',contex)

def karaoke(request,slug):
    song = Song.objects.filter(slug=slug).first()
    context = {'song':song}
    return render(request,'home/karaoke.html',context)

@csrf_exempt
def audiomarge(request):
    recorded_audio = request.FILES['audio']
    new = tempSong(tempSongFile=recorded_audio)
    new.tempSongFile.name = 'yo.wav'
    new.save()
    record_file_path = new.tempSongFile.url
    record_file_path = '.'+str(record_file_path)
    
    songslug = request.POST.get('songslug')
    current_song = Song.objects.filter(slug=songslug)[0]
    current_song_path = current_song.songFile.url 
    current_song_path = '.'+(str(current_song_path))
    
    input_first = ffmpeg.input(current_song_path)
    input_second = ffmpeg.input(record_file_path)


    ffmpeg.concat(input_first, input_second, v=0, a=1).output('media/home/music/okay.wav').run()
    
    return HttpResponse("good")

@csrf_exempt
def videomarge(request):
    recorded_video = request.FILES['video']
    new = tempSong(tempSongFile=recorded_video)
    new.tempSongFile.name = 'honeysing.webm'
    new.save()
    record_file_path = new.tempSongFile.url
    record_file_path = '.'+str(record_file_path)

    songslug = request.POST.get('songslug')
    current_song = Song.objects.filter(slug=songslug)[0]
    current_song_path = current_song.songFile.url 
    current_song_path = '.'+(str(current_song_path))
    
    input_first = ffmpeg.input(record_file_path)
    input_second = ffmpeg.input(current_song_path)
    try:
        ffmpeg.concat(input_first, input_second, v=1, a=1).output('media/home/music/okayvideo.webm').run()
        return HttpResponse("okay")
    except:    
        return HttpResponse('Failed!')



