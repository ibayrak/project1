# -*- coding: utf-8 -*-
from django.db import models
class Document(models.Model):
    docfile = models.FileField(upload_to='csv_uploads')

class Member(models.Model):
    name =models.CharField(max_length=200)
    surname=models.CharField(max_length=200)    
    email =models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
