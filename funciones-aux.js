import fs from 'fs';
import path from 'path';
import AdmZip from 'adm-zip';
import child_process from 'child_process';

export async function crearApp(){

    const comando = 'npm run build';
  
    try {
  
      const { stderr } = await child_process.execSync(comando);

      if (stderr) {
        console.error(`Error durante la ejecución:\n${stderr}`);
        return;
      }

      await crearZip();

    } catch (error) {
      console.error(`Error al ejecutar el comando: ${error}`);
    }
  
  }

async function crearZip() {
  
   const zip = new AdmZip()
   zip.addLocalFolder('./dist')
   zip.writeZip('dist.zip')
  
   return 'dist.zip'
}
  
export function crearJson(parhDirJson, fileName, datos){
    
    const filePath = path.join(parhDirJson, fileName); 
  
    try {
      const jsonData = JSON.stringify(datos, null, 2); 
      fs.writeFileSync(filePath, jsonData, { encoding: 'utf8' });
  
      console.log(`JSON file '${filePath}' created`);
  
    } catch (err) {
      console.error(`Error writing to file: ${err.message}`);
    }
  }