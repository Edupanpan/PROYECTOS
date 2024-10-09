import React from 'react'
import Navbar from './components/navbar/Navbar'
import {Routes, Route } from 'react-router-dom'
import Home from './components/pages/Home'
import Album from './components/pages/Album'

const App = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/album" element={<Album />} />
      </Routes>
    </>        
  )
}

export default App