from string import ascii_uppercase, ascii_lowercase, digits
import random

from django.http import HttpResponse

from .models import ShortUrl


def generate_short_url(url):
    # generate a 6-character code to be used for the short url
    short_code_list = [random.choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(6)]
    short_url_code = ''.join(short_code_list)

    # save original url and its associated short url code to db
    shorturl_obj = ShortUrl(original_url=url, short_url_code=short_url_code)
    shorturl_obj.save()

    return short_url_code

def load_url(short_url_code):
    try:
        # get object which matches the requested short url code
        shorturl_obj = ShortUrl.objects.get(short_url_code=short_url_code)

        # increment times used field by 1
        shorturl_obj.times_used += 1
        shorturl_obj.save()

        return shorturl_obj
    except ShortUrl.DoesNotExist:
        # return exception if the requested short url does not exist in db
        return HttpResponse('Exception: ShortUrl matching query does not exist')

def load_all_urls():
    # get all short url objects
    return ShortUrl.objects.all().order_by('original_url', '-created_at')