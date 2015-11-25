#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-25 15:52:59
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-25 15:58:33

class ForumRouter(object):
    """
    A router to control all database operations on models in the
    forum application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read forum models go to forum_db.
        """
        if model._meta.app_label == 'forum':
            return 'forum_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write forum models go to forum_db.
        """
        if model._meta.app_label == 'forum':
            return 'forum_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the forum app is involved.
        """
        if obj1._meta.app_label == 'forum' or \
           obj2._meta.app_label == 'forum':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the forum app only appears in the 'forum_db'
        database.
        """
        if app_label == 'forum':
            return db == 'forum_db'
        return None