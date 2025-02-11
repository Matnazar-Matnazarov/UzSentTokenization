
# Create your views here.
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
    # print(r)
    for i in r:
        t = i.lower()
        if t in sintaksis_dict or yuklama_check(t):
            a = True
            print(t, yuklama_check(t))
    return a

text = """
Bugun havo juda issiq. Men ertalab soat yettida turdim va nonushta qildim. Dada ishga ketdilar, onam esa uy ishlari bilan band edilar. Kecha do‘stlarim bilan futbol o‘ynadim, juda charchadik. Bu mashina juda tez yuradi, lekin haydovchisi ehtiyot bo‘lishi kerak. Biz maktabga borishimiz kerak edi, ammo yomg‘ir yog‘ib yubordi.

Sen ertaga qayerga borasan? Kecha kitobxonaga bordingmi? Shu kitobni menga bera olasanmi? Nega bugun juda jim o‘tiribsan? Sizning ismingiz nima? Bu masalani qanday yechish mumkin? Telefoningni topa olmadingmi? Bugun havo qanday bo‘ladi?

Voy, qanday chiroyli manzara! Qanday ajoyib yangilik! Nahotki sen bu narsani o‘ylab topding?! Tezroq yugur, poyezd ketib qoladi! Hushyor bo‘l, yo‘lda ehtiyot bo‘l! Yashasin bizning jamoamiz! Bu juda zo‘r film ekan!

"""

text_tokens = UST.tokenize(text)
for i in text_tokens:
    if func(i):
        print(i)