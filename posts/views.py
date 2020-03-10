from django.shortcuts import render
from .models import Post, Account
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import urllib.parse
#Main, I guess?
def index(request, u_id):
    latest_post_list = Post.objects.order_by('votes')
    out = ""
    for q in latest_post_list:
        if(q.to_show):
            out += (q.post_title+"<br>"+q.post_sub+"<br>"+q.post_text+"<br>"+str(q.id)+"<br>"+str(q.votes)+"<br>"+str(q.happy)+"<br>"+str(q.angry)+"<br>"+str(q.stressy)+"<br>"+str(q.energy)+"<br>"+str(q.worry)+"<br>"+q.poster+"<br>"+temp1(q, u_id)+"<hr>")
    return HttpResponse(out)
def make(request, title, body, sub, happ, angr, stress, energ, worr, posterID):
    try:
        i = Account.objects.get(pk=int(posterID))
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
    p = Post(post_title=unparse(title), post_text=unparse(body), post_sub=unparse(sub), pub_date=timezone.now(), happy=happyVar, angry=angryVar, stressy=stressyVar, energy=energyVar, worry=worryVar, poster=Account.objects.get(pk=posterID).uname)
    p.save()
    return HttpResponse("OK")
def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        return HttpResponse(q.post_title+"<br>"+q.post_sub+"<br>"+q.post_text+"<br>"+q.id+"<br>"+str(q.votes)+str(q.happy)+"<br>"+str(q.angry)+"<br>"+str(q.stressy)+"<br>"+str(q.energy)+"<br>"+str(q.worry)+"<br>"+q.poster)
    except Post.DoesNotExist:
        raise Http404("404")

def results(request, post_id):
    return HttpResponse(str(Post.objects.get(pk=post_id).votes))

def vote(request, post_id, updown, u_id):
    p = Post.objects.get(pk=post_id)
    downers = p.downers.split(",")
    uppers = p.uppers.split(",")
    if((u_id in uppers) and updown == "up"):
        print("in uppers")
    elif((u_id in downers) and updown == "down"):
        print("in downers")
    elif((u_id in downers) and updown == "up"):
        print("in downers, tryna up")
        downers.remove(str(u_id))
        p.votes += 2

    elif((u_id in uppers) and updown == "down"):
        print("in uppers, tryna down")
        uppers.remove(str(u_id))
        p.votes += (0-2)

    else:
        if(updown == "up"):
            p.votes += 1
            uppers.append(str(u_id))
            print("up")
        elif(updown == "down"):
            p.votes += -1
            downers.append(str(u_id))
            print("down")

    if(p.votes < (-10)):
        p.to_show = False
        print("No show"+p.post_title+" "+str(p.id))
    p.uppers = ','.join(upper)
    p.downers = ','.join(downer)
    p.save()
    return HttpResponse("OK")

def createAccount(request,name,word):
    try:
        i = Account.objects.get(uname=name)
        return HttpResponse("uname")
    except ObjectDoesNotExist:
        a = Account(uname=unparse(name),pword=unparse(word), signup_date=timezone.now())
        a.save()
        return HttpResponse(str(a.id))
def login(request, name,word):
    try:
        i = Account.objects.get(uname=unparse(name), pword=unparse(word))
        return HttpResponse(str(i.id))
    except ObjectDoesNotExist:
        return HttpResponse("nope")
def temp1(q, u_id):
    if (str(u_id) in q.uppers.split(',')):
        return "up"
    elif (str(u_id) in q.downers.split(',')):
        return "down"
    else:
        return "none"
def betterIndex(request,happ,angr,stress,worr,energ,start,len,u_id):
    latest_post_list = Post.objects.order_by('votes')[start:len]
    out = ""
    for q in latest_post_list:
        if(happ==1 and not q.happy):
            tempshow=False
        if(angr==1 and not q.angry):
            tempshow=False
        if(stress==1 and not q.stressy):
            tempshow=False
        if(worr==1 and not q.worry):
            tempshow=False
        if(energ==1 and not q.energy):
            tempshow=False
        if(q.to_show and tempshow):
            out += (q.post_title+"<br>"+q.post_sub+"<br>"+q.post_text+"<br>"+str(q.id)+"<br>"+str(q.votes)+"<br>"+str(q.happy)+"<br>"+str(q.angry)+"<br>"+str(q.stressy)+"<br>"+str(q.energy)+"<br>"+str(q.worry)+"<br>"+q.poster+"<br>"+temp1(q,u_id)+"<hr>")
    return HttpResponse(out)
def unparse(text):
    return urllib.parse.unquote_plus(urllib.parse.unquote(text))
