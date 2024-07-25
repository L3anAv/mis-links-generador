import { useEffect } from 'react'
import infoUser from "/opt/render/project/src/src/info/infoUser.json"
import Footer from "./components/footer/Footer"
import Links from "./components/links/Links"

function App() {
  
  const theme = new Map([
    ['dark', 'dark-theme'],
    ['ligh', 'light-theme']
  ])

  useEffect(() => {
    // > Para el nombre
    window.document.title = `🔗 Los links de ${infoUser[0].Name}`
    
    // Para el settear el theme
    window.document.body.classList = `${theme.get(infoUser[0].Theme)}`
    
  }, [])

  return (
    <div>
      <Links colorBottom={infoUser[0].ColorBottoms}/>
      <Footer />
    </div>
    
  )
}

export default App