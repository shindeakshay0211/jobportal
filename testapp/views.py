from django.shortcuts import render
from testapp.models import *

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')


def hydjobs_view(request):
    jobs_list=hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)


def mumbaijobs_view(request):
    jobs_list=mumbaijobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/mumbaijobs.html',context=my_dict)


def punejobs_view(request):
    jobs_list=punejobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',context=my_dict)
