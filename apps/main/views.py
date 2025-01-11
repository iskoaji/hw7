from django.shortcuts import render, redirect
from apps.main.models import Index, Steps, Contact, Form, Faq
from .service import get_text
# Create your views here.
def index(request):
    index = Index.objects.latest('id')
    steps = Steps.objects.all()
    return render (request, 'index.html', locals())

def about(request): 
    index = Index.objects.latest('id')
    return render(request, 'about-us.html', locals())

def faq(request):
    faqq = Faq.objects.all()
    return render(request, 'faq.html', locals())

def contact(request):
    contact = Contact.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Form.objects.create(name=name, email=email, message=message)
        
        get_text(f"""
Имя отправителя: {name}
email: {email}
Сообщение: {message}
""")
        return redirect('index')
    return render (request, 'contacts.html', locals())

