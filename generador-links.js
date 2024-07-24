import fs from 'fs';
import cors from 'cors';
import path from 'path';
import express from 'express';
import bodyParser from 'body-parser';
import {crearApp, crearJson } from './funciones-aux.js';


const app = express();
const nombreArchivo = 'dist.zip'
const pathActual = process.cwd()
const rutaArchivo = path.join(pathActual, nombreArchivo)

app.get('/', (_, res) => {
  res.send('¡Hola desde mi API Generador-Links');
});

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({ extended: true }));

app.use(cors({
  origin: 'https://generador-links.vercel.app/',
  methods: ['GET', 'POST'], 
  allowedHeaders: ['Content-Type', 'Authorization'], 
  exposedHeaders: ['Content-Range'],
}));

app.post('/', async (req, res) => {

    // Data
    const data = req.body

    // Datos
    const Nombre = data.Nombre
    const ColorTheme = data.ColorTheme.value
    const ColorBotones = data.ColorBotones.value

    const arrayRedes = data.redes

    // Datos config usuario
    const datos_usuario = [{
      "Name": Nombre,
      "Theme": ColorTheme,
      "ColorBottoms": ColorBotones,
    }]
    
    const targetDir = './src/info'
    const fileNameInfo = 'infoUser.json'; 
    const fileNameRedes = 'RutasLinks.json'

    // Creando json
    crearJson(targetDir, fileNameInfo, datos_usuario)
    crearJson(targetDir, fileNameRedes, arrayRedes)

    // Buildeando app
    await crearApp();

    if (fs.existsSync(rutaArchivo)) {
      return res.status(200).send()
    }else{
      return res.status(404).send()
    }

});

app.get('/descargar', (_, res) => {
  
  try {

    res.setHeader('Access-Control-Allow-Origin', 'https://generador-links.vercel.app/');
    res.setHeader('Access-Control-Allow-Methods', 'GET');
    res.setHeader('Content-Type', 'application/zip');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    res.setHeader('Content-Disposition', `attachment; filename=dist.zip`);

    if (fs.existsSync(rutaArchivo)) {
      res.download(rutaArchivo, nombreArchivo, (err) => {
        if (err) {
          console.error('Error al descargar el archivo:', err);
          res.status(500).send('Error al descargar el archivo');
          return;
        }
        console.log('Archivo descargado correctamente.');
      });
    } else {
      return res.status(404).send('Archivo no encontrado.');
    }
  } catch (error) {
    console.error(error);
    res.status(500).send('Error al descargar el archivo.');
  }
});

const port = process.env.PORT || 5000;

app.listen(port, () => {
  console.log(`Servidor escuchando en el puerto ${port}`);
});