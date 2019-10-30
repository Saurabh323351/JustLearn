#
from django.db import models
#
# import sys
# sys.path.append("/home/saurabh/Desktop/Folder/DjangoProjects/FundooNotes/Labels")


from Labels.models import *


from django.contrib.auth.models import User


class Note(models.Model):

    title=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    color=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    reminder=models.DateTimeField(null=True,blank=True)

    is_pinned=models.BooleanField(default=False)
    is_trashed=models.BooleanField(default=False)
    is_archived=models.BooleanField(default=False)
    collaborator=models.ManyToManyField(User,related_name='notes',blank=True)
    labels=models.ManyToManyField(Label,related_name='notes',blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    modified_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title