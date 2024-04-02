from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    techstack = models.CharField(max_length=50)



class ProjectList(models.Model):
    fkey = models.ForeignKey(CustomUser, related_name='projects_owned', on_delete=models.CASCADE)
    contributors = models.ManyToManyField(CustomUser, related_name='projects_contributed', blank=True)
    project_name = models.CharField(max_length=100)
    project_code = models.CharField(max_length=100, unique=True, null=True)  # Unique identifier for the project
    html_code = models.TextField(null=True)  # For storing HTML content
    css_code = models.TextField(null=True)  # For storing CSS content
    js_code = models.TextField(null=True)  # For storing JavaScript content
    status = models.BooleanField(default=False)
    
    @property   
    def CreaterID(self):
       return self.fkey.id

    def __str__(self):
        return self.project_name


class Project_History(models.Model):
   contributorId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   project_name = models.CharField(max_length=255)
   description = models.TextField()


   def __str__(self):
       return self.project_name


class Chat(models.Model):
   fkey = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   chatId = models.CharField(max_length = 10)
   message = models.CharField(max_length = 1000, null = True)


   @property
   def senderId(self):
       return self.fkey.userId
   def recieverID(self):
       return self.fkey.userId