from UzSentTokenization import UzSentTokenizer as UST
from .models import UzSentTokenization, Yuklamalar


def func3(s:str):
    a = set(Yuklamalar.objects.values_list('word_yuklamalar', flat=True))
    for i in a:
        if s.endswith(i):
            return True
    return False


def func(s:str):
    if not s:  # Bo'sh matn tekshiruvi
        return False
        
    a, r = False, []
    k = ""
    for i in s:
        if i == " " or i == "." or i == "," or i == "!" or i == "?":
            if k != "": 
                r.append(k)
                k = ""
        else:
            k += i
    
    # Oxirgi so'zni qo'shish
    if k:
        r.append(k)
        
    # So'zlar ro'yxati bo'sh bo'lsa
    if not r:
        return False
        
    sintaksis_dict = set(UzSentTokenization.objects.values_list('word', flat=True))
    for i in r:
        t = i.lower()
        if t in sintaksis_dict:
            a = True
            
    # Oxirgi so'zni tekshirish
    if r and func3(r[-1]):  # r bo'sh emasligini tekshiramiz
        a = True
    return a


def func2(text):
    if not text:  # Bo'sh matn tekshiruvi
        return [], []
        
    a, r = [], []
    tokens = UST.tokenize(text)
    
    if not tokens:  # Tokenlar bo'sh bo'lsa
        return [], []
        
    for i in tokens:
        if func(i):
            k = i
            if not i.endswith('?'):
                for p in '.!':
                    if p in k:
                        k = k.replace(p, '')
                k += '?'
            a.append(k)
        else:
            if i.endswith('?'):
                r.append(i)
    return a, r