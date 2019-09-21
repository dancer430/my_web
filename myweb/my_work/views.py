from django.shortcuts import render


# Create your views here.
def my_work_home(request):
    return render(request, 'index.html')
