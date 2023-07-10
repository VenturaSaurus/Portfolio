# hola, este proyecto se trata de un lector de codigo de barras en imagenes proporcionadas, a continuacion se proveera mas informacion

from pyzbar import pyzbar
from PIL import Image

def scan_barcodes(image_path):
    # Abrir la imagen
    with open(image_path, 'rb') as image_file:
        image = Image.open(image_file)
        # Convertir la imagen a escala de grises
        gray_image = image.convert('L')
    
    # Obtener los códigos de barras en la imagen que se requiere
    barcodes = pyzbar.decode(gray_image)

    # Iterar sobre los códigos de barras encontrados
    for barcode in barcodes:
        # Decodificar el código de barras y obtener su tipo y datos
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        
        # Mostrar el resultado en la consola
        print("Tipo de código de barras: {}, Datos: {}".format(barcode_type, barcode_data))

# Ruta de la imagen que deseas escanear
image_path = "ruta_de_la_imagen.jpg"

# Llamar a la función para escanear los códigos de barras
scan_barcodes(image_path)
