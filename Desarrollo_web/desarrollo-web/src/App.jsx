import React from 'react'
import {Routes, Route } from 'react-router-dom'
import Home from './components/pages/Home'
import Album from './components/pages/Album'
import Mapa from './components/pages/Mapa'

const App = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/album" element={<Album />} />
        <Route path="/mapa" element={<Mapa />} />
      </Routes>
    </>        
  )
}

export default App