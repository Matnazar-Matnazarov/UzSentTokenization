from django.core.management.base import BaseCommand
from app.models import UzSentTokenization, Yuklamalar

class Command(BaseCommand):
    help = 'Creates initial tokens for UzSentTokenization'
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        a = set(Yuklamalar.objects.values_list('word_yuklamalar', flat=True))
        sintaksis_dict = {
    "nima", "nimani", "nimaning", "nimada", "nimadan", "nimalar", "nimasi", "ne", "kimni", "kimning", "kimga", "kimda", "kimdan", "kimlar", "kimim", "kiming", "kimi", "kim", "qanday", "qanaqa", "qaysi", "qay", "qalay", "qani", "qayer", "qachon", "qay kuni", "qay vaqt", "qanaqasi", "qaysisi", "qaysinisi", "qaysilari", "qandayi", "qay holatda", "qay ko'rinishda", "qayerga", "qayerda", "qayerdan", "qachondan", "qachonlar", "qay vaqtda",
    "nega", "nimaga", "nima uchun", "qay sababdan", "nechada", "nechtadan", "qanchadan", "nechinchi", "qay maqsadda", "nima qil",
    "nima qildim", "nima qilding", "nima qildik", "nima qildingiz", "nima qildilar",
    "nima qilyapman", "nima qilyapsan", "nima qilyapti", "nima qilyapmiz", "nima qilyapsiz", "nima qilyaptilar",
    "nima qilaman", "nima qilasan", "nima qiladi", "nima qilamiz", "nima qilasiz", "nima qilasizlar", "nima qiladilar",
            "nima bo'l", "nima bo'ldi", "nima bo'lyapti", "nima bo'ladi"
        }
        b = set(UzSentTokenization.objects.values_list('word', flat=True))
        yuklama = {'mi','-chi','-ya'} 
        for i in sintaksis_dict:
            if i not in a:  
                UzSentTokenization.objects.create(word=i)
           
        for i in yuklama:
            if i not in b:
                Yuklamalar.objects.create(word_yuklamalar=i)
        self.stdout.write(self.style.SUCCESS('Successfully created tokens'))
    