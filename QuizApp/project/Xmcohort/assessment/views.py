from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from pytube import YouTube
import os
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings as django_settings
import wave
import speech_recognition as sr
from django.core.files.storage import default_storage
from .models import *
import speech_recognition as spr
from urllib import parse
import requests as requests
import re
import base64
import gspread
r = sr.Recognizer()


def createquestion(request):
  if request.method == "POST":
    print(request.POST)
    form = addQuestionform(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  else:
      form = addQuestionform()

  return render(request, 'createquestion.html', {'form': form})


def addcandidate(request):
  if request.method == "POST":
    form = addcandidateform(request.POST)
    if form.is_valid():
      form.save()
      print("sva")
      return redirect('/')
  else:
      form = addcandidateform()

  return render(request, 'addcandidate.html', {'form': form})

 
        

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            p=request.POST.get(q.Qques)
            print(p)
            print(q.QAnswer)
            if q.QAnswer ==  request.POST.get(q.Qques):
                correct+=1
                score+=1
            else:
                wrong+=1
        gc = gspread.service_account(filename='credentials.json')
        sh = gc.open_by_key('1tDmzc-_PhH1H6Vj8bUM56odqR_ub3X6eYjzRgzQ-w5A')
        worksheet = sh.sheet1
        user = [str(request.user), str(score)]
        worksheet.append_row(user)
              
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        
        questions=question.objects.all()
        cand=candidate.objects.all()
        p=0
        for q in cand:
            if(q.candidate_id==request.user):
                user=q.author
                print(user)
                return render(request,'sample.html',{'ques':questions, 'us': user})
       
        return render(request,'sample.html',{'ques':questions, 'us': p})

       
       
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'accounts/login.html',context)

def logoutPage(request):
    logout(request)
    context={}
    return render(request,'accounts/login.html',context)


def index(request):
  if request.method == 'POST':
    print(request.POST)
    form = UploadForm(request.POST,request.FILES or None )
    if form.is_valid():
      form.save()
      return redirect('/')
  else:
      form = UploadForm()

  return render(request, 'viva.html', {'form': form})

def show(request):
    if request.method == 'POST' :
       
        questions=viva.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            file= request.FILES[q.ques]
            print(file)
            print(q.ques)
            aobj = Audio()
            aobj.name='temp'
            aobj.option = file
            aobj.save()
            audio=Audio.objects.last()
            print(audio.option)
            adurl = str(audio.option.url)
            ##print(adurl[1:])
            fs=FileSystemStorage()
            fs.save(file.name,file)
            
            with spr.WavFile(adurl[1:]) as source:
                audio_data1 = r.record(source)
                text1 = r.recognize_google(audio_data1)
                print(text1)
            with spr.WavFile(q.ans) as source:
                audio_data = r.record(source)
                text = r.recognize_google(audio_data)
                print(text) 


            
           
            if text ==  text1:
                correct+=1
                score+=1
            else:
                wrong+=1
            
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'total':total
        }

        gc = gspread.service_account(filename='credentials.json')
        sh = gc.open_by_key('1jcVjXatBdxCkbgB1FfIzeHTV7zhTHhbgPQcICGwqofQ')
        worksheet = sh.sheet1
        user = [str(request.user), str(score)]
        worksheet.append_row(user)
        return render(request,'result.html',context)
    else:
        
        questions=viva.objects.all()
        cand=candidate.objects.all()
        p=0
        for q in cand:
            if(q.candidate_id==request.user):
                user=q.author
                print(user)
                return render(request,'showviva.html',{'p':questions, 'us': user})
       
        return render(request,'showviva.html',{'p':questions, 'us': p})


def viewresult(request):
    context={}
    return render(request,'viewresult.html',context) 


    


    

