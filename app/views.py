from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import UzSentTokenization, Yuklamalar
from .utils import func2
import pandas as pd

class YuklamalarView(View):
    def get(self, request):
        yuklamalar = Yuklamalar.objects.all()
        return render(request, 'yuklamalar.html', {'yuklamalar': yuklamalar})
    def post(self, request):
        word = request.POST.get('word')
        if word:
            Yuklamalar.objects.create(word_yuklamalar=word)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Word is required'})
    def delete(self, request, id):
        try:
            yuklama = Yuklamalar.objects.filter(id=id).first()
            if yuklama:
                yuklama.delete()
                return JsonResponse({'status': 'success'})
            return JsonResponse({'status': 'error', 'message': 'Word not found'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    

class UzSentTokenizationView(View):
    def get(self, request):
        uzsenttokenization = UzSentTokenization.objects.all()
        return render(request, 'uzsenttokenization.html', {'uzsenttokenization': uzsenttokenization})
    def post(self, request):
        word = request.POST.get('word')
        if word:
            UzSentTokenization.objects.create(word=word)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Word is required'})
    def delete(self, request, id):
        try:
            UzSentTokenization.objects.filter(id=id).first().delete()
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error', 'message': 'Word not found'})
    

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        text = request.POST.get('text')
        tokens = func2(text)
        return JsonResponse({'status': 'success', 'tokens': tokens[0], 'error_tokens': tokens[1]})
    

class CreateTokenView(View):



    def get(self, request):
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
    
        return JsonResponse({'status': 'success'})
    

class IndexImportView(View):
    def post(self, request):
        try:
            file = request.FILES.get('file')
            if not file:
                return JsonResponse({'status': 'error', 'message': 'Fayl tanlanmagan'})

            text = ""
            if file.name.endswith('.txt'):
                text = file.read().decode('utf-8')
            elif file.name.endswith('.docx'):
                import docx
                doc = docx.Document(file)
                text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
            else:
                return JsonResponse({
                    'status': 'error', 
                    'message': 'Faqat .txt va .docx fayllari qo\'llab-quvvatlanadi'
                })

            return JsonResponse({
                'status': 'success',
                'text': text
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Xatolik yuz berdi: {str(e)}'
            })
    