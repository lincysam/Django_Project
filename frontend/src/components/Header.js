import React from 'react'
import { Container } from 'react-bootstrap'

const Header = ({header}) => {
  return (
    <div>
    {header.map((heading) => (

   
    <div>
        <Container>
        <h1 >{heading.name}</h1>
       
        </Container>
    </div>
  ))

    }
    </div>
  )
}

export default Header