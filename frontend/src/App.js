
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Brandlist from './components/Brandlist';
import {BrowserRouter as Router,Route, Routes } from 'react-router-dom';
import Addbrand from './components/Addbrand';
import Menu from './components/Menu';
import Home from './components/Home';
import Header from './components/Header';



function App() {
  
  return (
    <div className="App">
      <Router>
        <Menu />
        
        <Routes>
             <Route path="/" element={<Home/>} />
            <Route path="/brandlist" element={<Brandlist/>} />
          	<Route path="/addbrand" element={<Addbrand/>} />
            
            

        </Routes>
      </Router>
     
    </div>
  );
}

export default App;
