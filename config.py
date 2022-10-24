#DEMO

import os
import json
import pathlib

rutaActual = pathlib.Path().absolute()

#Nombre para pag de liks
nombre = input('Your Name: ')

#Theme del proyecto
print('\nThemes options:\n\x1b[38;5;9m 1) dark \033[0m \n\x1b[38;5;9m 2) light \033[0m', end='\n')
theme = input("\nTheme: ")

#Color para botones
# blue, orange, purple, green & pink.
print('\nColor for bottoms: \n\x1b[38;5;81m 0) blue \033[0m \n\x1b[38;5;214m 1) orange \033[0m \n\x1b[38;5;141m 2) purple \033[0m \n\033[0;32m 3) green \033[0m \n\x1b[38;5;199m 4) pink \033[0m', end='\n')
botomColor = input("\nColor: ")

#Seteo de json para theme e info de usuario
dataInfoUser = {}
info = [{"Name": nombre, "Theme": theme, "ColorBottoms": botomColor}]
dataInfoUser = info
file = "InfoUser.json"

rutaParaArchivo = str(rutaActual) + "/src/info"

with open(os.path.join(rutaParaArchivo, file), 'w') as jsonSalida:
    json.dump(dataInfoUser, jsonSalida)