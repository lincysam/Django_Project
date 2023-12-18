import React from 'react'
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import showroom from '../image/showroom.jpg';
import {Image} from "react-bootstrap";

import Header from './Header';

const Home = () => {
  const header = [
		{name : "Mobile Showroom"},
		]
  return (
    <div>
    <Header header={header}/>
    
    <Image src={showroom}  thumbnail/>
    </div>
    
  
    

  )
}

export default Home