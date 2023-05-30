from django.shortcuts import render

# Create your views here.
def wish(request):
    dict={'a':10,'b':20}
    return render(request,'wish.html', context=dict)