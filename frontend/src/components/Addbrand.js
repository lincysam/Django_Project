import { useState} from "react"
import React from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom';




const Addbrand = () => {
    const [brand_image,setImage]= useState(null)
    const[brandname,setName]= useState("")
   

    
    const navigate = useNavigate();


    const AddbrandInfo= async () => {
      let formField = new FormData()
      formField.append('brandname',brandname)
      
      if(brand_image !==null){
        formField.append('brand_image',brand_image)
         }

      
      
      await axios({
        method:'post',
        url:'http://localhost:8000/showroom/',
        data:formField
        }).then ((response) =>{
        console.log(response.data);
        navigate('/')
        
        })
         
    }



  return (
    
      
      <div className="Container">
     
      <div className="form-group"> 
       
        <div className="form-group">
        <h1 className="header">Create Brand</h1>
           <input type="text" className="form-control form-control-Ig" placeholder="Enter Brand Name"
              name="brandname" value={brandname}
               onChange={(e) => setName(e.target.value)} />
        </div>
        
        
        <div className="form-group">
              
              <input type="file" className="form-control form-control-Ig" 
              name="brand_image" 
               onChange={(e) => setImage(e.target.files[0])} />
        </div>
        <div>
          
        </div>
        
        <button className="btn btn-success" onClick={AddbrandInfo}>Save</button>

      </div>

    </div>
    
    
   
  )
}

export default Addbrand