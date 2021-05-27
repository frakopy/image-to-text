from PIL import Image
import pytesseract,os
from colorama import Fore, init, Style

init(autoreset=True)

imagenes = dict(enumerate(os.listdir('D:\A_PYTHON\ProgramasPython\Convertir_Imagen_a_Texto\imagenes')))

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\tesseract.exe'


path_archivoTxt = 'D:/A_PYTHON/ProgramasPython/Convertir_Imagen_a_Texto/textoDeImagen.txt'

titulo = Fore.LIGHTGREEN_EX+'''
### # #  #   ## ###      ##  #  ### # # ### ##   ##  #  ##
 #  ### # # #   #       #   # # # # # # #   # # #   # # # #
 #  ### ### # # ##      #   # # # # # # ##  ##   #  # # ##
 #  # # # # # # #       #   # # # # # # #   # #   # # # # #
### # # # #  ## ###      ##  #  # #  #  ### # # ##   #  # #
'''

conversion = False
continuar = 's'
while conversion == False and continuar == 's':
    
    os.system('cls')# limipiamos la pantalla para comenzar a imprimir nuevamente el menu

    try:         
        print(titulo)
        Texto_Extraido = open(path_archivoTxt, 'w')
        
        print(Fore.LIGHTGREEN_EX+'SELECCIONA EL NUMERO QUE CORRESPONDE A LA IMAGEN'.center(70,'*')+'\n') 
        for numero,nombre in imagenes.items():
            print()
            num_imagen = str(numero)+' ---> '+nombre.upper()
            print(Style.BRIGHT+num_imagen)
        print()    
        seleccion = int(input())
        path_imagen = 'D:/A_PYTHON/ProgramasPython/Convertir_Imagen_a_Texto/imagenes/'+imagenes[seleccion]
        achivo_imagen = Image.open(path_imagen)
        texto = pytesseract.image_to_string(achivo_imagen)
        texto = texto.replace('-\n',' ')

        Texto_Extraido.write(texto)
        Texto_Extraido.close()
        print('\n\n'+Fore.LIGHTYELLOW_EX+'SE HA REALIZADO LA CONVERSION CON EXITO\n')
        os.startfile('D:/A_PYTHON/ProgramasPython/Convertir_Imagen_a_Texto/textoDeImagen.txt')
        
        print(Style.BRIGHT+'¿Desea convertir mas imagenes (S/N)?:\n')
        continuar = input().lower()#Convertimos a minuscula lo ingresado por el usuario
        if continuar == 's':
            conversion = False
        else:
            conversion = True
    except:
        print()
        print(Fore.LIGHTRED_EX+'Numero de la imagen incorrecto\n')
        print(Style.BRIGHT+'¿Desea intentar nuevamente (S/N) ?\n')
        continuar = input().lower()
