#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-25 15:52:59
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-25 16:05:57

class BattleRouter(object):
    """
    A router to control all database operations on models in the
    battle application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read battle models go to battle_db.
        """
        if model._meta.app_label == 'battle':
            return 'battle_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write battle models go to battle_db.
        """
        if model._meta.app_label == 'battle':
            return 'battle_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the battle app is involved.
        """
        if obj1._meta.app_label == 'battle' or \
           obj2._meta.app_label == 'battle':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the battle app only appears in the 'battle_db'
        database.
        """
        if app_label == 'battle':
            return db == 'battle_db'
        return None
