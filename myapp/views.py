from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')


@login_required
def home(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        response = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + name)
        o = response.json()
        tracks_info = []
        for result in o['results']:
            track_info = {
                'trackname':result['trackName'],
                'previewUrl':result.get('previewUrl','')
            }
            tracks_info.append(track_info)
        context = {'tracks_info': tracks_info}
    return render(request, 'myapp/home.html', context)

