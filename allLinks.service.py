import os
import json
import shutil
import pathlib
from flask_cors import CORS
from flask import Flask, request, render_template, redirect, url_for, send_file, jsonify, make_response

#Nombres de json
fileLinks = "RutasLinks.json"
fileInfoUser = "InfoUser.json"

#Obtener la ruta actual
rutaActual = pathlib.Path().absolute()

#Setear la ruta para los archivos
rutaParaArchivo = str(rutaActual) + "/src/info"

#Setear la ruta para los archivos
rutaParaComprimir = str(rutaActual) + "/dist"

#Ruta Archivo zip
rutaZip = str(rutaActual) + "/dist.zip"

project_root = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=project_root)
CORS(app, origins=['*'], expose_headers=['Content-Disposition'])

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
    if initial_count >= 2:
        os.system('npm run build')
        print('\n >> Su proyecto se creo exitosamente en: ' + str(rutaActual) + '/dist')
        print('¡¡ Gracias por usar !! <3\n')
    else:
        sys.exit('\n\x1b[38;5;9mOcurrio un error. No se han creado los archivos necesarios para crear el proyecto.\033[0m')

#Funcion para comprimir la carpeta dist
def comprimir():
    shutil.make_archive('dist', 'zip', rutaParaComprimir)
    return "Creacion satisfactoria"

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':

        datos_redes = []
        data = request.get_json()
        arrayRedes = data["redes"]
        nombre = data['Nombre']
        color_theme = data['ColorTheme']
        color_botones = data['ColorBotones']

        print(arrayRedes)
        
        #Rellenar el datos_redes
        for red in arrayRedes:
            nombreRed = red["nombre"]
            rutaRed = red["ruta"]

            diccionario_red = {
                "nombre": nombreRed,
                "ruta": rutaRed
            }

            datos_redes.append(diccionario_red)
        
        # Crear el datos_usuarios
        datos_usuario = [{
            "Name": nombre,
            "Theme": color_theme,
            "ColorBottoms": color_botones,
        }]

        #Creacion de jsons
        crearJson(rutaParaArchivo, fileInfoUser, datos_usuario)
        crearJson(rutaParaArchivo, fileLinks, datos_redes)

        #Crea la app
        crearApp()

        #Response
        response_data = {
        'message': 'ENVIADO',
        'processed_data': data
        }

        return jsonify(response_data)
    else:
        return render_template('index.html')

@app.route('/descargar', methods=['GET'])
def comprimir_y_descargar():
    try:
        comprimir()
        # Comprimir archivos and prepare data for download (replace with your logic)
        if not os.path.exists(rutaZip):
            raise Exception('Compressed file not found!')  # Handle missing file
        #os.path.basename(rutaZip)
        response = make_response(send_file(rutaZip, as_attachment=True))
        response.headers['Content-Disposition'] = f'attachment; filename="{os.path.basename(rutaZip)}"'  # Set filename
        
        return response

    except Exception as e:
        # Handle errors gracefully (e.g., log error, return appropriate HTTP status code)
        print(f"Error downloading file: {e}")
        return 'Error downloading file!', 500


if __name__ == '__main__':
    app.run(debug=True)