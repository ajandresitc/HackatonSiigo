from PIL import Image
import pytesseract
import os
import ast


clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
clear()
img = 'img1.png'
contenido = pytesseract.image_to_string(Image.open(img))
# print contenido.splitlines()
InfoFactura = {}

c = 0
tokens=['TOTAL','CLIENTE','FECHA','IVA','IMPUESTO','SUBTOTAL','VENDEDOR','NIT','DIRECCION','RESOLUCION','FACTURA']
for i in contenido.splitlines():
    c=c+1
    if c==1: InfoFactura['Razon social'] = i.encode('utf8')
    for j in tokens:
        if j in i.upper(): InfoFactura[j] = i.encode('utf8')


contenidoXY = (pytesseract.image_to_data(Image.open(img)))

detalle=0
InfoDetalle = {}

c = 0
for i in contenido.splitlines():
    if 'CANT' in i.upper(): detalle=1 # x inferior
    if 'TOTAL' in i.upper() and not detalle: detalle=0 # x superior
    if detalle:
        c=c+1
        InfoDetalle['Detalle'+ str(c)] = i.encode('utf8')
InfoFactura['Detalle'] = InfoDetalle
print InfoFactura