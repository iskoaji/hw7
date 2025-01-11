from django.core.management.base import BaseCommand
from apps.main.service import bot

class Command(BaseCommand):
    help = 'Bot'
    
    def handle(self, *args, **options):
        print("START TELEGRAM BOT")
        bot.polling(none_stop=True, interval=0)