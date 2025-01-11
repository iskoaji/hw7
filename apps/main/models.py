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
    
    name_des = models.CharField(
        max_length=255,
        verbose_name='Тема описания'
    )
    
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    
    description = models.TextField(
        verbose_name='Описание'
    )
    
    title2 = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    
    description2 = models.TextField(
        verbose_name='Описание'
    )
    
    numl = models.CharField(
        max_length=255,
        verbose_name='Нумерация'
        
    )
    
    name_desl = models.CharField(
        max_length=255,
        verbose_name='Тема описания'
    )
    
    
    titlel = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    
    descriptionl = models.TextField(
        verbose_name='Описание'
    )
    
    title2l = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    
    description2l = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return f'{self.img}'
    
    class Meta:
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги'

class Contact(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    fb = models.URLField(
        verbose_name='Facebook'
    )
    ig = models.URLField(
        verbose_name='Instagram'
    )
    tt = models.URLField(
        verbose_name='TikTok'
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=255
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        
class Form(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    message = models.TextField(
        verbose_name="Введите сообщение"
    )
    
    def __str__(self):
         return self.name
     
    class Meta:
        verbose_name = "Оставленный отзыв"
        verbose_name_plural = 'Оставленные отзывы'
        
class TelegramUser(models.Model):
    id_user = models.CharField(
        max_length=100,
        verbose_name="ID пользователя telegram"
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя",
        blank=True, null=True
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
        blank=True, null=True
    )
    chat_id = models.CharField(
        max_length=100,
        verbose_name="Чат ID"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        return str(self.username)
    
    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграма"
