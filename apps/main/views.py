from django.shortcuts import render
from apps.main.models import Index, Steps
# Create your views here.
def index(request):
    index = Index.objects.latest('id')
    steps = Steps.objects.all()
    return render (request, 'index.html', locals())

def about(request):
    index = Index.objects.latest('id')
    return render(request, 'about-us.html', locals())
