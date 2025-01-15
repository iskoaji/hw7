from django.contrib import admin
from apps.main.models import Index, Steps, Contact, Faq
from django.utils.html import format_html
# Register your models here.

admin.site.register(Index)
admin.site.register(Faq)



@admin.register(Steps)
class StepsAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height=50px />'.format(obj.img.url))
    
    image_tag.short_description = 'Фото'
    
    list_display = ('title', 'image_tag',)
    # search_fields = ['title']
    # list_display = ['title']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("title", 'description')