from pywebio.output import put_html, put_file
from pywebio.session import hold
from frontend import getInfo
from backend import fillDoc

title = "<h1 style=\"text-align:center\">O'zbekiston Respublikasi fuqorosining\
    xorijga chiqish biometrik pasportini rasmiylashtirish uchun ANKETA</h1>"
put_html(title)    
    
userInfo = getInfo()
filename = fillDoc(userInfo)

text = "<h3>Anketa tayyor. Yuklab olish uchun quyidagi bog'lamani bosing.</h3>"
put_html(text)

with open(filename, 'rb') as fayl:
    anketa = fayl.read()
    put_file(filename, content=anketa)
    hold()



