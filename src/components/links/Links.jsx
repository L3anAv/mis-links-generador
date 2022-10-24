import './links.css'
import '/src/theme.css'
import RutasLinks from '/src/info/RutasLinks.json'

//import { FaInstagram } from 'react-icons/fa';

function Links(colorBottom){
  /* Bottom Colors: blue, orange, purple, green & pink. */

  const colores = new Map([
    ['blue', 'button-c-blue'],
    ['orange', 'button-c-orange'],
    ['purple','button-c-purple'],
    ['green', 'button-c-green'],
    ['pink', 'button-c-pink']
  ]);

  return (
    <div>
      <h1>🔗 Mis redes 🔗</h1>
      {RutasLinks.map(value => <a href={value.Ruta} target="_blank"><button className={colores.get(colorBottom.colorBottom)}>{value.Nombre}</button></a>)}
    </div>
  )
}

export default Links