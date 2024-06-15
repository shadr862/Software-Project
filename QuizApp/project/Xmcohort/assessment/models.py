
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings




class question(models.Model):
    Qid = models.AutoField(primary_key=True)
    User = settings.AUTH_USER_MODEL
    User_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Qques = models.TextField(max_length=200,null=True)
    Qoption1 = models.TextField(max_length=200,null=True)
    Qoption2 = models.TextField(max_length=200,null=True)
    Qoption3 = models.TextField(max_length=200,null=True)
    Qoption4 = models.TextField(max_length=200,null=True)
    QAnswer = models.TextField(max_length=200,null=True)
    def __str__(self):
        return self.Qques



class result(models.Model):
    result = models.AutoField(primary_key=True)
    User_id = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.FloatField()


def __str__(self):
    return str(self.pk)




class candidate(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_by', on_delete=models.CASCADE)
    candidate_id = models.OneToOneField(User, on_delete=models.CASCADE)
    
def __str__(self):
    return str(self.pk) 



class viva(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    ques = models.FileField(upload_to='media')
    ans  = models.FileField(upload_to='media')
    
    
def __str__(self):
    return str(self.pk)


class Audiomodel(models.Model):
    op  = models.FileField(upload_to='media')
    
    
def __str__(self):
    return str(self.pk)


class Audio(models.Model):
    name = models.TextField(max_length=200,null=True)
    option  = models.FileField(upload_to='Audio')
    
    
def __str__(self):
    return str(self.pk)



