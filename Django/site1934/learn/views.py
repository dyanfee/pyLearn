# coding:utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


# def index(request):
#     return HttpResponse(u"hello Django!")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))


def index(request):
    # tutorialList = ["HTML","CSS3","jQuery","Python","Django"]
    # return render(request,"home.html",{'TutorialList': tutorialList})
    # info_dict = {'site': u"free id", "content": u"学习而战"}
    # return render(request, "home.html", {'info_dict': info_dict})

    Lis = map(str,range(100))
    return render(request,"home.html",{"lis":Lis})


def reverse_test(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )
