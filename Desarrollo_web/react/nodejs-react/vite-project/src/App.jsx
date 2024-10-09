import React, { useState } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const containerStyle = {
  width: '100%',
  height: '400px'
};

const center = {
  lat: -3.745, // Latitud inicial
  lng: -38.523 // Longitud inicial
};

const MapComponent = () => {
  const [location, setLocation] = useState(center);
  const [address, setAddress] = useState('');

  const handleSearch = async () => {
    const response = await fetch(`https://maps.googleapis.com/maps/api/geocode/json?address=${encodeURIComponent(address)}&key=YOUR_API_KEY`);
    const data = await response.json();

    if (data.results.length > 0) {
      const { lat, lng } = data.results[0].geometry.location;
      setLocation({ lat, lng });
    } else {
      alert('No se encontró la dirección.');
    }
  };

  return (
    <div>
      <input
        type="text"
        value={address}
        onChange={(e) => setAddress(e.target.value)}
        placeholder="Buscar dirección"
      />
      <button onClick={handleSearch}>Buscar</button>
      <LoadScript googleMapsApiKey="YOUR_API_KEY">
        <GoogleMap
          mapContainerStyle={containerStyle}
          center={location}
          zoom={15}
        >
          <Marker position={location} />
        </GoogleMap>
      </LoadScript>
    </div>
  );
};

export default MapComponent;