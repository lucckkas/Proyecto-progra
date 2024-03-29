import os

def abrir(dir1, dir2):
    # recibe un dir2 que deberia ser una subcarpeta o archivo de dir1
    # retorna un string con la direccion completa de dir2
    return os.path.join(dir1, dir2)
def tanque(num):
    if num == 1:
        return abrir(carpeta_base,tank1)
    elif num == 2:
        return abrir(carpeta_base,tank2)
def cagnon(num):
    if num == 1:
        return abrir(carpeta_cagnon,mira1)
    elif num == 2:
        return  abrir(carpeta_cagnon,mira2)
def num(num):
    if  num == 0:
        return abrir(carpeta_numeros,"0.png")
    elif  num == 1:
        return abrir(carpeta_numeros,"1.png")
    elif num == 2:
        return abrir(carpeta_numeros, "2.png")
    elif num == 3:
        return abrir(carpeta_numeros, "3.png")
    elif num == 4:
        return abrir(carpeta_numeros, "4.png")
    elif num == 5:
        return abrir(carpeta_numeros, "5.png")
    elif num == 6:
        return abrir(carpeta_numeros, "6.png")
    elif num == 7:
        return abrir(carpeta_numeros, "7.png")
    elif num == 8:
        return abrir(carpeta_numeros, "8.png")
    elif num == 9:
        return abrir(carpeta_numeros, "9.png")
def txt(texto):
    if texto == "distancia":
        return abrir(carpeta_texto,"distan.png")
    elif texto == "balas":
        return abrir(carpeta_texto,"balas.png")
    elif texto == "potencia":
        return abrir(carpeta_texto,"power.png")
    elif texto == "altura":
        return  abrir(carpeta_texto,"height.png")


#nombres archivos
tank1="tank1.png"
tank2="tank2.png"
mira1="canon1.png"
mira2="canon2.png"


# rutas archivos
# carpeta principal
carpeta_archivos = abrir(os.path.dirname(__file__), "Archivos")
# imagenes
carpeta_imagenes = abrir(carpeta_archivos, "Imagenes")  # carpeta con todas las sub carpetas de imgs

carpeta_balas = abrir(carpeta_imagenes, "Balas")
carpeta_explosiones = abrir(carpeta_imagenes, "Explosiones")

carpeta_tanke = abrir(carpeta_imagenes, "Tanke")  # carpeta con sub carpetas de los tankes
carpeta_base = abrir(carpeta_tanke, "Base")
carpeta_cagnon = abrir(carpeta_tanke, "Cagnon")

carpeta_boton = abrir(carpeta_imagenes, "Botones")

carpeta_texto = abrir(carpeta_imagenes, "Texto")  # carpeta con los textos largos y sub carpeta con  los numeros
carpeta_numeros = abrir(carpeta_texto, "Numeros")

carpeta_sonidos = abrir(carpeta_archivos, "Sonidos")

# CONSTANTES
GRAVEDAD_TIERRA = 9.80665
FPS = 60

# COLORES
BLANCO = [255, 255, 255]
NEGRO = [0, 0, 0]
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]
AZUL = [0, 0, 255]

# variables
# terreno
tamagno_mapa = [1280, 720]
forma_terreno = 5
largo_mitad = 640
alto = 720

grosor = 2
# tanke
vida_tanke = 100
balas_60mm = 3
balas_perforantes = 10
balas_105mm = 3
# bala dmg
dagno_60mm = 30
dagno_perforante = 40
dagno_105mm = 50
# bala tamagno explosion
tam_exp_60mm = 40
tam_exp_perforante = 60
tam_exp_105mm = 80

# volumen
Vbala1 = 0.1
Vbala2 = 0.1
Vbala3 = 0.1
VHell = 0.2
VGreat = 0.2
VMusica = 0.02
