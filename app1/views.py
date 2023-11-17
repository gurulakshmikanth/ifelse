from django.shortcuts import render

# Create your views here.
def compare(request):
    d={'a':10,'b':50}
    return render(request,'compare.html',d)
