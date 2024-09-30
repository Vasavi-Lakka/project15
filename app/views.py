from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn=input('enter topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        topics=Topic.objects.all()
        d={'topics':topics}
        return render(request,'displayTopic.html',d)
        #return HttpResponse("New object is created")
    else:
        return HttpResponse("Already Exits")


def insert_webpage(request):
    tn=input('enter topic name: ')
    n=input('Enter name: ')
    u=input('enter url: ')

    QLTO=Topic.objects.filter(topic_name=tn)

    if QLTO:
        TO=QLTO[0]
        WO=webpage.objects.get_or_create(topic_name=TO, name=n, url=u)
        webpages=webpage.objects.all()
        d={'webpages': webpages}
        return render(request,'displayWebpage.html',d)
        #return HttpResponse("New object is created")
    else:
        return HttpResponse("Already Exits")
    
def insert_AccessRecord(request):
    tn=input('enter topic name: ')
    n=input('Enter name: ')
    a=input("Enter author: ")
    d=input('enter date: ')
    u=input('enter url: ')

    QLTO=Topic.objects.filter(topic_name=tn)
    #QLWO=webpage.objects.filter(topic_name=QLTO, name=n, url=u)
    if QLTO:
        TO=QLTO[0]
        QLWO=webpage.objects.filter(topic_name=TO, name=n, url=u)
        #return HttpResponse("Created new object")
        if QLWO:
            WO=QLWO[0]
            AO=AccessRecord.objects.get_or_create(topic_name=TO, url=WO ,name=WO, author=a, date=d)
            accessrecord=AccessRecord.objects.all()
            d={'accessrecord':accessrecord}
            #return render(request, 'displayAccessrecord.html', d)

            return HttpResponse("Created new object")
        else:
            return HttpResponse("Already Exits")
    else:
        return HttpResponse("Data is not available")




def displayTopic(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'displayTopic.html',d)

def displayWebpage(request):
    webpages=webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'displayWebpage.html',d)

def displayAccessrecord(request):
    accessrecord=AccessRecord.objects.all()
    d={'accessrecord': accessrecord}
    return render(request, 'displayAccessrecord.html',d)
                  
                  
                  
'''
def insert_topic(request):
    tn=input('enter topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        return HttpResponse("New object is created")
    else:
        return HttpResponse("Already Exits")

def insert_webpage(request):
    tn=input('enter topic name: ')
    n=input('Enter name: ')
    u=input('enter url: ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=webpage.objects.get_or_create(topic_name=TO, name=n, url=u)
    if WO[1]:
        return HttpResponse("New object is created")
    else:
        return HttpResponse("Already Exits")

def insert_AccessRecord(request):
    tn=input('enter topic name: ')
    n=input('Enter name: ')
    a=input("Enter author: ")
    d=input('enter date: ')
    u=input('enter url: ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=webpage.objects.get_or_create(topic_name=TO, name=n, url=u)[0]

    AO=AccessRecord.objects.get_or_create(name=WO, author=a, date=d)

    if AO[1]:
        return HttpResponse("New object is created")
    else:
        return HttpResponse("Already Exits")'''