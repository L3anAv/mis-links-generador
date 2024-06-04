import './links.css'
import '/src/theme.css'
import RutasLinks from '../../info/RutasLinks.json'

function Links(colorBottom){

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
      {RutasLinks.map(value => <a href={value.ruta} target="_blank"><button className={colores.get(colorBottom.colorBottom)}>{value.nombre}</button></a>)}
    </div>
  )
}

export default Links