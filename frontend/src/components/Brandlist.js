import React,{useState,useEffect} from 'react'
import axios from 'axios';
import {Card,Button} from  'react-bootstrap';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Header from './Header';
import {Link} from 'react-router-dom';

const Brandlist = () => {
    const header = [
		{name : "Brand List"}
		]
    const [brands,setBrands] = useState([])

    const getbrands = async () => {
        const response = await axios.get('http://localhost:8000/showroom/')
        setBrands(response.data)
    }
    useEffect(() =>{
        getbrands();
    },[]
    )

  return (
    
   <section>
    <Header header={header} />
    <Container fluid>
        <div className='title-holder'>
           
        </div>
    <Row>{
        brands.map(brand => {
            return(
      <Col sm={4} key={brand.id}>
            <div className='card-style'>
                    {
                       
                        <Card className="m-2 rounded shadow-lg ">
                            <Card.Img variant="top" src={brand.brand_image} style={{height:'15rem',width:'25rem'}}  />
                                <Card.Body>
                                    <Card.Title>{brand.brandname}</Card.Title>
                                    
                                    <Link className='btn btn-primary' to={'/${brand.id}/modellist'}>Show Details</Link>
                                </Card.Body>
                        </Card>
                            
                            
            
                    }
          </div>
      </Col>)
})}
    </Row>
  </Container>
  </section>


   
    
  )
}

export default Brandlist