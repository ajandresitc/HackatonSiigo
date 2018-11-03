from PIL import Image
import pytesseract
import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
clear()
contenido = pytesseract.image_to_string(Image.open('img2.png'))
# print contenido.encode('utf8')
# print contenido.splitlines()
InfoFactura = {}

c = 0
detalle=0
tokens=['TOTAL','FECHA','IVA','IMPUESTO']
for i in contenido.splitlines():
    c=c+1
    if c==1: InfoFactura['Razon social'] = i.encode('utf8')
    for j in tokens:
        if j in i.upper(): InfoFactura[j] = i.encode('utf8')
    if 'CANT' in i.upper(): detalle=1
    if 'TOTAL' in i.upper() and not detalle: detalle=0
    if detalle: 
        InfoFactura['Detalle'+ str(c)] = i.encode('utf8')
print InfoFactura