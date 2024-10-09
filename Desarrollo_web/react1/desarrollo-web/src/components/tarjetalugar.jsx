
import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
const TarjetaLugar = ({ lugares }) => {
  return (
    <>
      <ul className="list-unstyled">
      {lugares.map((lugar) => {
      const fechaFormateada = lugar.fechavisita.slice(0, 10); // Extrae los primeros 10 caracteres
      return (
        <div className='bg-white mb-4'>

          <li key={lugar.id} className="lead " style={{ color: 'black', marginBottom: '20px' }}>
          <h2>{lugar.nombre}</h2>
          <img src={lugar.imagen} alt={lugar.nombre} className="img-fluid d-block mb-2" />
          <p>{fechaFormateada}</p>
          <p>{lugar.direccion}</p>
          </li>
        </div>
      );
      })}
      </ul>
    </>
    );
};

export default TarjetaLugar;
