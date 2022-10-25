#DEMO
import os
import json
import pathlib
import sys

rutaActual = pathlib.Path().absolute()

#Nombre para pag de liks
nombre = input('Your Name: ')

#Theme del proyecto
themes = ['dark', 'light']
print('\nThemes options:\n\x1b[38;5;9m 1) dark \033[0m \n\x1b[38;5;9m 2) light \033[0m', end='\n')
themeOpcion = int(input("\nIngresar numero de opcion: "))


if themeOpcion <= 2:
    theme = themes[themeOpcion-1]
else:
    sys.exit('Opcion no valida.')

#Color para botones ># blue, orange, purple, green & pink.
colores = ['blue', 'orange', 'purple','green', 'pink']
print('\nColor for bottoms: \n\x1b[38;5;81m 1) blue \033[0m \n\x1b[38;5;214m 2) orange \033[0m \n\x1b[38;5;141m 3) purple \033[0m \n\033[0;32m 4) green \033[0m \n\x1b[38;5;199m 5) pink \033[0m', end='\n')
colorOption = int(input("\nIngresar numero de opcion: "))

if colorOption <= 5:
    botomColor = colores[colorOption-1]
else:
    sys.exit('Opcion no valida.')
    

#Seteo de json para theme e info de usuario
dataInfoUser = {}
info = [{"Name": nombre, "Theme": theme, "ColorBottoms": botomColor}]
dataInfoUser = info
file = "InfoUser.json"

rutaParaArchivo = str(rutaActual) + "/src/info"

with open(os.path.join(rutaParaArchivo, file), 'w') as jsonSalida:
    json.dump(dataInfoUser, jsonSalida)