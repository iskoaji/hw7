from django.db import models

# Create your models here.

class Index(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка главной страницы'
        verbose_name_plural = 'Настройки главной страницы'
        
class Steps(models.Model):
    img = models.ImageField(
        upload_to='steps/',
        verbose_name='Фото'
    )
    num = models.CharField(
        max_length=255,
        verbose_name='Нумерация'
        
    )
    
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    
    description = models.TextField(
        verbose_name='Описание'
    )
    
    
    def __str__(self):
        return f'{self.img}'
    
    class Meta:
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги'