from UzSentTokenization import UzSentTokenizer as UST

sintaksis_dict = {
    "nima", "nimani", "nimaning", "nimada", "nimadan", "nimalar", "nimasi", "ne", "kimni", "kimning", "kimga", "kimda", "kimdan", "kimlar", "kimim", "kiming", "kimi", "kim", "qanday", "qanaqa", "qaysi", "qay", "qalay", "qani", "qayer", "qachon", "qay kuni", "qay vaqt", "qanaqasi", "qaysisi", "qaysinisi", "qaysilari", "qandayi", "qay holatda", "qay ko'rinishda", "qayerga", "qayerda", "qayerdan", "qachondan", "qachonlar", "qay vaqtda",
    "nega", "nimaga", "nima uchun", "qay sababdan", "nechada", "nechtadan", "qanchadan", "nechinchi", "qay maqsadda", "nima qil", 
    "nima qildim", "nima qilding", "nima qildik", "nima qildingiz", "nima qildilar",
    "nima qilyapman", "nima qilyapsan", "nima qilyapti", "nima qilyapmiz", "nima qilyapsiz", "nima qilyaptilar",
    "nima qilaman", "nima qilasan", "nima qiladi", "nima qilamiz", "nima qilasiz", "nima qilasizlar", "nima qiladilar",
    "nima bo'l", "nima bo'ldi", "nima bo'lyapti", "nima bo'ladi"
}

def yuklama_check(s:str):
    for i in ['mi', 'chi', 'ya',]:
        if s.endswith(i):
            return True
    return False

def func(s:str):
    
    a,r = False,[]
    k = ""
    for i in s:
        if i == " " or i == "." or i == "," or i == "!" or i == "?":
            if k != "": 
                r.append(k)
                k = ""
        else:
            k += i
    for i in r:
        t = i.lower()
        if t in sintaksis_dict or yuklama_check(t):
            a = True
    return a

def func2(text):
    return [i for i in UST.tokenize(text) if func(i)]