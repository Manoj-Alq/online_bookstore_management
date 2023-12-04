import React from 'react'
import { BrowserRouter as Router, Route, Routes, useNavigate, Navigate } from 'react-router-dom'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Home from './layouts/Home'
import Header from './components/Header';
import './App.css'
import Login from './layouts/Login';

const App = () => {
  return (
    <>
      <Router>
          <div className='overflow-x-hidden containerfluid'>
            <Header />
            <Routes>
              <Route path='/' element={ <Home /> }/>
              <Route path='/login' element={ <Login /> }/>
            </Routes>
          </div>
      </Router>
    </>
  )
}

export default App
