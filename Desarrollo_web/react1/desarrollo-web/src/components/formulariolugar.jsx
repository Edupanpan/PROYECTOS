// FormularioLugar.js
import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

const FormularioLugar = ({ onAgregarLugar }) => {
  const [nombre, setNombre] = useState('');
  const [fecha, setFecha] = useState('');
  const [imagen, setImagen] = useState('');

  const manejarEnvio = (e) => {
    e.preventDefault();
    const nuevoLugar = { nombre, fecha, imagen };
    onAgregarLugar(nuevoLugar);
    // Limpiar el formulario
    setNombre('');
    setFecha('');
    setImagen('');
  };

  return (
    <Form onSubmit={manejarEnvio}>
      <Form.Group controlId="formNombre">
        <Form.Label>Nombre del Lugar</Form.Label>
        <Form.Control 
          type="text" 
          placeholder="Ingresa el nombre del lugar" 
          value={nombre} 
          onChange={(e) => setNombre(e.target.value)} 
          required 
        />
      </Form.Group>
      <Form.Group controlId="formFecha">
        <Form.Label>Fecha de Visita</Form.Label>
        <Form.Control 
          type="date" 
          value={fecha} 
          onChange={(e) => setFecha(e.target.value)} 
          required 
        />
      </Form.Group>
      <Form.Group controlId="formImagen">
        <Form.Label>URL de la Imagen</Form.Label>
        <Form.Control 
          type="text" 
          placeholder="Ingresa la URL de la imagen" 
          value={imagen} 
          onChange={(e) => setImagen(e.target.value)} 
          required 
        />
      </Form.Group>
      <Button variant="primary" type="submit">
        Agregar Lugar
      </Button>
    </Form>
  );
};

export default FormularioLugar;
