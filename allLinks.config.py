#imports
from ctypes.wintypes import PINT
import os
import json
import pathlib
import sys

#Variables/otros necesarios
infoLinks = []
continuar = True
themes = ['dark', 'light']
repo  =  ['GitHub', 'GitLab']
social = ['Instagram', 'Twitter', 'repo']
colors = ['blue', 'orange', 'purple','green', 'pink']

#Obtener la ruta actual
#Setear la ruta para los archivos
rutaActual = pathlib.Path().absolute()
rutaParaArchivo = str(rutaActual) + "/src/info"

#Retorna el valor correspondiente seleccionado por el ususario
def controlarValorIngresado(userIngressInt, maxValue, array):
    if userIngressInt <= maxValue:
        value = array[themeOpcion-1]
        return value
    else:
        sys.exit('\n\x1b[38;5;9mSe ingreso un opcion no valida.\033[0m')

#Funcion para crear los json necesarios para el proyecto.
def crearJson(path, nameOfJson, dataForJson):
    with open(os.path.join(path, nameOfJson), 'w') as jsonSalida:
        json.dump(dataForJson, jsonSalida)

#Corre los comandos para crear el proyecto

def crearApp():
     #Cuento cantidad de archivos
    initial_count = 0
    for path in pathlib.Path(rutaParaArchivo).iterdir():
        if path.is_file():
            initial_count += 1

    #Comprobacion de cantidad de archivos y corro comandos
    if initial_count == 2:
        os.system('npm run build')
        print('\n >> Su proyecto se creo exitosamente en: ' + str(rutaActual) + '/dist')
    else:
        sys.exit('\n\x1b[38;5;9mOcurrio un error. No se han creado los archivos necesarios para crear el proyecto.\033[0m')

def mostarPreview(boolean):
    if boolean:
        os.system('npm run preview')


#Configuraciones previas
os.remove(rutaParaArchivo + '/vacio.txt')
os.system('npm install')

#Nombre para la pagina
print('\n --- TODOS TUS LINKS --- \n')
nombre = input('Ingresa tu nombre: ')

#Elegir el color del theme
print('\nThemes options:\n\x1b[38;5;9m 1) Oscuro \033[0m \n\x1b[38;5;9m 2) Claro \033[0m', end='\n')
themeOpcion = int(input("\nIngrese el numero de opcion elegida: "))
theme = controlarValorIngresado(themeOpcion, len(themes), themes)


#Elegrir color de botones
print('\nColors for bottoms: \n\x1b[38;5;81m 1) Azul \033[0m \n\x1b[38;5;214m 2) Naranja \033[0m \n\x1b[38;5;141m 3) Violeta \033[0m \n\033[0;32m 4) Verde \033[0m \n\x1b[38;5;199m 5) Rosa \033[0m', end='\n')
colorOption = int(input("\nIngrese el numero de opcion elegida: "))
botomColor = controlarValorIngresado(colorOption, len(colors), colors)

#Creacion de json: InfoUser
Jsoninfo = {}
dataInfoUser = [{"Name": nombre, "Theme": theme, "ColorBottoms": botomColor}]
Jsoninfo = dataInfoUser
fileInfoUser = "InfoUser.json"
crearJson(rutaParaArchivo, fileInfoUser, Jsoninfo)

#Peticion de usuarios/otros para links de botones    
while(continuar):
    dataLinks = {}
    for item in social:
        if item != 'repo':
            user = input('Ingresa tu @ para ' + item + ' (sin el @): ')
            link = 'https://www.' + item + '.com/' + user
            infoLinks.append({'name': item, 'ruta': link})
        else:
            print('Reposity GitHub or GitLab?\n')
            print('Options: \n\x1b[38;5;0m 1) Github \033[0m \n\x1b[38;5;214m 2) GitLab \033[0m')
            repoOption = int(input('\nIngrese el numero de opcion elegida: '))
            repository = controlarValorIngresado(repoOption, len(repo), repo)
            user = input('Ingresa tu @ para ' + repository + ' (sin el @): ')

            if repository == 'GitHub':
                link = 'https://www.' + repository + '.com/' + user
            else:
                link = 'https://www.' + repository + '.io/' + user
            infoLinks.append({'name': repository,'ruta': link})

    continuar = False

#Creacion de json: RutasLinks
fileLinks = "RutasLinks.json"
crearJson(rutaParaArchivo, fileLinks, infoLinks)

#Correr app si todo lo necesario esta
crearApp()

valor = input('¿Quiere ver un preview del proyecto? [s/n]: ')

if valor == 's':
    mostarPreview()
else:
    sys.exit('¡¡ Gracias por usar !!')