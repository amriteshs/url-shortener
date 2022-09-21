import json

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from .service import load_url, generate_short_url, load_all_urls

# Create your views here.
def index(request):
    return render(request, 'index.html')

def url_shorten(request):
    # url to be shortened is received as a post request
    original_url = request.POST['url']

    if not original_url:
        return redirect('index')

    # generate short url code and build the short url
    short_url_code = generate_short_url(original_url)
    short_url = request.build_absolute_uri(reverse('redirect_url', args=[short_url_code]))
    
    return render(request, 'short_url.html', {'original_url': original_url, 'short_url': short_url})

def redirect_url(request, short_url_code):
    # query the object associated with the short url code
    shorturl_obj = load_url(short_url_code)

    # if the requested short url does not exist
    if isinstance(shorturl_obj, HttpResponse):
        return shorturl_obj

    # redirect to original url
    return redirect(shorturl_obj.original_url)

def show_url_list(request):
    # get all the url objects
    shorturl_objs = load_all_urls()
    url_list = []

    for obj in shorturl_objs:
        # build url for short url code
        shortened_url = request.build_absolute_uri(reverse('redirect_url', args=[obj.short_url_code]))
        
        # convert datetime.datetime object to string
        creation_datetime = obj.created_at.strftime('%d/%m/%Y, %H:%M:%S')

        # url data for front-end display
        url_data = {
            'original_url': obj.original_url,
            'short_url': shortened_url,
            'created_at': creation_datetime,
            'times_used': obj.times_used
        }

        # append to list of url objects
        url_list.append(url_data)

    return render(request, 'url_list.html', {'url_list': url_list})
    