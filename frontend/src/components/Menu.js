import React from 'react'
import {Navbar,Nav,Container} from 'react-bootstrap';
import { NavLink } from 'react-router-dom';

const Menu = () => {
  return (
    <div>
        <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
       
          
          <Nav className="me-auto">
          
          <NavLink className="brand-list-nav" to="/">Home</NavLink>
            <NavLink className="add-brand-nav" to="/addbrand">Create Brand</NavLink>
            <NavLink className="add-brand-nav" to="/createmodel">Create Model</NavLink>
            <NavLink className="brand-list-nav" to="/brandlist">Brand List</NavLink>
            
           
          </Nav>
          <Nav className='justify-content-end'>
          <NavLink className="brand-list-nav" to="/login">Login/Register</NavLink>
          </Nav>
        
        
      </Container>
    </Navbar>

    </div>
  )
}

export default Menu