from django.test import TestCase

from .models import ShortUrl
from .service import generate_short_url

# Create your tests here.
class ShortUrlTestCase(TestCase):
    def setUp(self):
        self.original_url_list = [
            'https://boardgamegeek.com/browse/boardgame',
            'https://gamepress.gg/pokemongo/pvp-stat-product-calculator#/',
            'https://boardgamegeek.com/browse/boardgame'
        ]

        for url in self.original_url_list:
            generate_short_url(url)

        self.duplicate_url = 'https://boardgamegeek.com/browse/boardgame'

    # test creation of objects in the database
    def test_short_url_objs_created(self):
        self.assertEqual(len(ShortUrl.objects.all()), 3)

    # test for the length of the short url code generated (should be equal to 6)
    def test_short_url_length(self):
        for shorturl_obj in ShortUrl.objects.all():
            self.assertEqual(len(shorturl_obj.short_url_code), 6)

    # test that short url codes for the same original url, but created at different times, are different
    def test_short_url_diff(self):
        short_urls = [shorturl_obj.short_url_code for shorturl_obj in ShortUrl.objects.filter(original_url=self.duplicate_url)]
        self.assertEqual(len(short_urls), len(set(short_urls)))
