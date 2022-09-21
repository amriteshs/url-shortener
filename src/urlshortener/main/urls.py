from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('url-shorten', views.url_shorten, name='url_shorten'),
    path('all-urls', views.show_url_list, name='show_all_urls'),
    path('<str:short_url_code>', views.redirect_url, name='redirect_url')
]