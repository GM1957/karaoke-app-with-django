from django.shortcuts import render, HttpResponse
from . models import Song

# Create your views here.
def home(request):
    allsongs = Song.objects.all()
    contex = {'allsongs': allsongs}
    return render(request, 'home/home.html',contex)

def karaoke(request,slug):
    song = Song.objects.filter(slug=slug).first()
    context = {'song':song}
    return render(request,'home/karaoke.html',context)