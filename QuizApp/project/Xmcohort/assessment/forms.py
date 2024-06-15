from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 



class addQuestionform(ModelForm):
    class Meta:
        model=question
        fields="__all__"



class result(ModelForm):
    class Meta:
        model=result
        fields="__all__"


class addcandidateform(ModelForm):
    class Meta:
        model=candidate
        fields = [
            "author",
            "candidate_id"
           ]


 
class UploadForm(ModelForm):
    class Meta:
        model = viva
        fields = [
            "author",
            "ques",
            "ans"
           ]


