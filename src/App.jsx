import { useEffect } from 'react'
import infoUser from './info/InfoUser.json'
import Footer from "./components/footer/Footer"
import Links from "./components/links/Links"

/* 
* Theme: dark || light.
* Name of the onwer: string.
* Require social media links in rutasLinks file.
* Configure the automatic configuration of the repo for deploy in pages gihub or gitlab.
*/

function App() {
  
  const theme = new Map([
    ['dark', 'dark-theme'],
    ['ligh', 'light-theme']
  ])

  

  useEffect(() => {
    window.document.title = `🔗 Los links de ${infoUser[0].Name}`
   

    // For control theme of the project
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
