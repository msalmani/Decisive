#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:56:38 2016

@author: mehdi
"""
from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.UploadView.as_view()), url(r'fileUpload$', views.UploadView.as_view()),]
