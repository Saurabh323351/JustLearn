from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


# class Label(models.Model):
#     name = models.CharField(max_length=150)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
# 
#     def __str__(self):
# 
#         return self.name

# 
# class Note(models.Model):
# 
#     title=models.CharField(max_length=500)
#     description=models.CharField(max_length=500)
#     color=models.CharField(max_length=300)
#     image=models.ImageField(upload_to='images/')
#     reminder=models.CharField(max_length=500,blank=True)
# 
#     is_pinned=models.BooleanField(default=False)
#     is_deleted=models.BooleanField(default=False)
#     is_archived=models.BooleanField(default=False)
#     collaborator=models.ManyToManyField(User)
#     labels=models.ManyToManyField(Label)
# 
#     modified_at=models.DateTimeField(auto_now=True)
#     created_at=models.DateTimeField(auto_now_add=True)
# 
# 
#     def __str__(self):
#         return self.title