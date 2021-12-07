import os


def abrir(dir1, dir2):
    # recibe un dir2 que deberia ser una subcarpeta o archivo de dir1
    # retorna un string con la direccion completa de dir2
    return os.path.join(dir1, dir2)


def tanque(numero):
    return abrir(carpeta_base, f"tank{numero}.png")


def cagnon(numero):
    return abrir(carpeta_cagnon, f"canon{numero}.png")


def num(numero):
    return abrir(carpeta_numeros, f"{numero}.png")


def txt(texto):
    if texto == "distancia":
        return abrir(carpeta_texto, "distan.png")
    elif texto == "balas":
        return abrir(carpeta_texto, "balas.png")
    elif texto == "potencia":
        return abrir(carpeta_texto, "power.png")
    elif texto == "altura":
        return abrir(carpeta_texto, "height.png")


# nombres archivos
tank1 = "tank1.png"
tank2 = "tank2.png"
tank3 = "tank3.png"
tank4 = "tank4.png"
tank5 = "tank5.png"
tank6 = "tank6.png"
mira1 = "canon1.png"
mira2 = "canon2.png"
mira3 = "canon3.png"
mira4 = "canon4.png"
mira5 = "canon5.png"
mira6 = "canon6.png"


# rutas archivos
# carpeta principal
carpeta_archivos = abrir(os.path.dirname(__file__), "Archivos")
# imagenes
carpeta_imagenes = abrir(carpeta_archivos, "Imagenes")  # carpeta con todas las sub carpetas de imgs

carpeta_balas = abrir(carpeta_imagenes, "Balas")
carpeta_explosiones = abrir(carpeta_imagenes, "Explosiones")
carpeta_bandera = abrir(carpeta_imagenes, "Bandera")

carpeta_tanke = abrir(carpeta_imagenes, "Tanke")  # carpeta con sub carpetas de los tankes
carpeta_base = abrir(carpeta_tanke, "Base")
carpeta_cagnon = abrir(carpeta_tanke, "Cagnon")

carpeta_boton = abrir(carpeta_imagenes, "Botones")

carpeta_texto = abrir(carpeta_imagenes, "Texto")  # carpeta con los textos largos y sub carpeta con  los numeros
carpeta_numeros = abrir(carpeta_texto, "Numeros")

carpeta_sonidos = abrir(carpeta_archivos, "Sonidos")

# CONSTANTES
GRAVEDAD_TIERRA = 9.8
FPS = 60

# COLORES
BLANCO = [255, 255, 255]
NEGRO = [0, 0, 0]
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]
AZUL = [0, 0, 255]
GRIS = [220, 220, 220]
GRIS2 = [190, 190, 190]

# variables
# terreno
tamagno_mapa = [800, 800]
forma_terreno = 5
grosor = 2

viento = 0
efecto_entorno = True
# tanke
cantidad_tankes = 5
balas_60mm = 10
balas_perforantes = 10
balas_105mm = 10

cantidad_IA = 0
# bala dmg
dagno_60mm = 30
dagno_perforante = 40
dagno_105mm = 50
# bala tamagno explosion
tam_exp_60mm = 30
tam_exp_perforante = 45
tam_exp_105mm = 60

# volumen
Vbala1 = 0
Vbala2 = 0
Vbala3 = 0
VHell = 0
VGreat = 0
VMusica = 0
