import React from 'react'

const Createmodel = () => {
  return (
    <div>
        <div>
            <h1>Create Model</h1>
        </div>
        <div className="Container">
      <div className="form-group">
       
        <div className="form-group">
           <input type="text" className="form-control form-control-Ig" placeholder="Enter Model Name"
              name="modelname" value={modelname}
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
    
    
    </div>
  )
}

export default Createmodel