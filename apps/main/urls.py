from django.urls import path
from apps.main.views import index, about, contact, faq, aboutme

urlpatterns = [
    path ('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq' ),
    path('aboutme/', aboutme, name='aboutme')
]

