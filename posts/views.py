from django.shortcuts import render
from .models import Post, Account
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
#Main, I guess?
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')
    out = ""
    for q in latest_post_list:
        if(q.to_show):
            out+=(q.post_title+"<br>"+q.post_sub+"<br>"+q.post_text+"<br>"+str(q.id)+"<br>"+str(q.votes)+"<br>"+str(q.happy)+"<br>"+str(q.angry)+"<br>"+str(q.stressy)+"<br>"+str(q.energy)+"<br>"+str(q.worry)+"<br>"+Account.objects.get(pk=q.poster).uname+"<hr>")
    return HttpResponse(out)
def make(request, title, body, sub, happ, angr, stress, energ, worr, posterID):
    try:
        i = Account.objects.get(pk=id)
    except ObjectDoesNotExist:
        return HttpResponse("invalid")
    happyVar=False
    angryVar=False
    stressyVar=False
    energyVar=False
    worryVar=False
    if(happ==1):
        happyVar=True
    if(angr==1):
        angryVar=True
    if(stress==1):
        stressyVar=True
    if(energ==1):
        energyVar=True
    if(worr==1):
        worryVar=True
    p = Post(post_title=title, post_text=body, post_sub=sub, pub_date=timezone.now(), happy=happyVar, angry=angryVar, stressy=stressyVar, energy=energyVar, worry=worryVar, poster=Account.objects.get(pk=posterID).uname)
    p.save()
    return HttpResponse("OK")
def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        return HttpResponse(q.post_title+"<br>"+q.post_sub+"<br>"+q.post_text+"<br>"+str(q.id)+"<br>"+str(q.votes)+str(q.happy)+"<br>"+str(q.angry)+"<br>"+str(q.stressy)+"<br>"+str(q.energy)+"<br>"+str(q.worry)+"<br>"+q.poster)
    except Post.DoesNotExist:
        raise Http404("404")

def results(request, post_id):
    return HttpResponse(str(Post.objects.get(pk=post_id).votes))

def vote(request, post_id, updown):
    p = Post.objects.get(pk=post_id)
    if(updown == "up"):
        p.votes += 1
        print("up")
    elif(updown == "down"):
        p.votes += -1
        print("down")

    if(p.votes < (-10)):
        p.to_show = False
        print("No show"+p.post_title+" "+str(p.id))
    p.save()
    return HttpResponse("OK")

def createAccount(request,name,word):
    try:
        i = Account.objects.get(uname=name)
        return HttpResponse("uname")
    except ObjectDoesNotExist:
        a = Account(uname=name,pword=word, signup_date=timezone.now())
        a.save()
        return HttpResponse(str(a.id))
def login(name,word):
    if(Account.objects.get(uname=name,pword=word).exists()):
        return HttpResponse(str(Account.objects.get(uname=name,pword=word).id))
    else:
        return HttpResponse("invalid")
