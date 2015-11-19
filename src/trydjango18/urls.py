"""trydjango18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from newsletter import views as news_views
from trydjango18 import views as trydjango18_views
from accounts import urls as accounts_urls


urlpatterns = [
	url(r'^$', news_views.home, name='home'),
	url(r'^contact/$', news_views.contact, name='contact'),
    url(r'^about/$', trydjango18_views.about, name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(accounts_urls, namespace='accounts'))
    #url(r'^accounts/', include('registration.backends.default.urls'))
]


'''You would NEVER do this in a production environment, however for the purposes of this
project we will use settings.DEBUG like this.'''
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
