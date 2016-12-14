from __future__ import unicode_literals

from django.db import models
import uuid,datetime
# Create your models here.


class User(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userName = models.CharField(max_length=200)
    password = models.CharField(max_length=200)#Fix the minimum length
    email = models.CharField(max_length=200)#Fix the minimum length

class Picture (models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    path = models.CharField(max_length=400)
    uploadDate = models.DateTimeField(null = True,blank=True)
    ownerID = models.ForeignKey(User)
    
class Comparison(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pictureID = models.ForeignKey(Picture)
    uploadDate = models.DateTimeField(null = True,blank=True)

class UserRating (models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score = models.IntegerField()
    raterID = models.ForeignKey(User)
    pictureID = models.ForeignKey(Picture)
    ratingDate = models.DateTimeField(null = True,blank=True)
    comparisonID = models.ForeignKey(Comparison)
    
class UserComment(models.Model):
    userID = models.UUIDField(default=uuid.uuid4, editable=True)
    comment = models.CharField(max_length=1000)#Fix the minimum length
    comparisonID = models.ForeignKey(Comparison)
    commentDate = models.DateTimeField(null = True,blank=True)

class ComparisonURL(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comparisonID = models.ForeignKey(Picture)
    URL = models.CharField(max_length=300)
    
    
#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#
#
#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)