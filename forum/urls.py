#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-10 16:55:44
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-12 14:27:31

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from forum import views, connection, profile, forum, errors

urlpatterns = [
	url(r'^$', views.index, name='forumindex'),
    url(r'^forumError/$', connection.indexError, name='indexError'),
    
    url(r'^subscribe/$', connection.subscribe, name='subscribe'),
    url(r'^connect/(?P<ref>.{0,50})/$', connection.connect, name='connect'),
    url(r'^logout/(?P<ref>.{0,50})/$', connection.disconnect, name='logout'),

    url(r'^profile/$', profile.profile, name='profile'),
    url(r'^profileinfos/(?P<profile_id>[0-9]+)/$', profile.profile_infos, name='profileinfos'),

    url(r'^forum/$', forum.forum, name='forum'),
    url(r'^subject/(?P<subject_id>[0-9]+)/$', forum.subject, name='subject'),
    url(r'^addsubject/(?P<subtheme_id>[0-9]+)/$', forum.addsubject, name='addsubject'),

    url(r'^test/$', views.test, name='test'),
    url(r'^deleteForum/$', views.deleteForum, name='delete'),
] + static(settings.FORUM_UPLOAD_URL, document_root=settings.FORUM_UPLOAD_ROOT)

handler404 = errors.error_404
handler500 = errors.error_500