"""MyDjangoSite URL Configuration

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

from forum import views, connection, profile, forum, errors
from MyDjangoSite.views import big_index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', big_index, name='big_index'),

    # FORUM APPLI URLS 
    url(r'^forum/$', views.index, name='index'),
    
    url(r'^forum/subscribe/$', connection.subscribe, name='subscribe'),
    url(r'^forum/connect/$', connection.connect, name='connect'),
    url(r'^forum/logout/$', connection.disconnect, name='logout'),

    url(r'^forum/profile/$', profile.profile, name='profile'),

    url(r'^forum/forum/$', forum.forum, name='forum'),
    url(r'^forum/subject/(?P<subject_id>[0-9]+)/$', forum.subject, name='subject'),
    url(r'^forum/addsubject/(?P<subtheme_id>[0-9]+)/$', forum.addsubject, name='addsubject'),

    url(r'^forum/test/$', views.test, name='test'),
    url(r'^forum/deleteForum/$', views.deleteForum, name='delete'),

] + static(settings.FORUM_UPLOAD_URL, document_root=settings.FORUM_UPLOAD_ROOT)

handler404 = errors.error_404
handler500 = errors.error_500