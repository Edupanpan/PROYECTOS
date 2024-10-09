import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Row, Col, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom'; // Importa useNavigate
import './Album.css'; 
import 'bootstrap/dist/css/bootstrap.min.css';
import TarjetaLugar from '../tarjetalugar'; 
import FormularioLugar from '../formulariolugar'; 

const Album = () => {
  const [lugares, setLugares] = useState([]);
  const [mostrarLugares, setMostrarLugares] = useState(false); 
  const [mostrarFormulario, setMostrarFormulario] = useState(false); 
  const navigate = useNavigate(); // Define navigate

  // Función para obtener datos de MockAPI
  const obtenerDatos = () => {
    axios.get('https://66fd61c7699369308954fd8e.mockapi.io/lugares/visita')
      .then((response) => {
        setLugares(response.data); // Almacena los datos extraídos de mockapi
      })
      .catch((error) => {
        console.error("Error al obtener los datos: ", error); // Maneja errores
      });
  };

  useEffect(() => { // Utiliza el hook de React useEffect para el proceso de conexión con mockapi
    obtenerDatos();
  }, []);

  const tohome = () => {
    navigate('/'); // Navega a la ruta home
  };

  const VerLugares = () => {
    setMostrarLugares(true); // Muestra el componente TarjetaLugar
    setMostrarFormulario(false); // Asegúrate de ocultar el formulario
  };

  const NuevoLugar = () => {
    setMostrarFormulario(true); // Muestra el formulario
    setMostrarLugares(false); // Asegúrate de ocultar los lugares
  };

  const agregarLugar = (nuevoLugar) => {
    setLugares((prevLugares) => [...prevLugares, nuevoLugar]);
    setMostrarFormulario(false); // Oculta el formulario después de agregar
  };

  return (
    <Container className="d-flex flex-column vh-100">
      <Row className="text-center mb-4">
        <h1 className="display-4">Mis Lugares</h1>
      </Row>
      <Row className="text-center mb-4">
        <Col>
          <Button onClick={tohome}>Home</Button>
        </Col>
        <Col>
          <Button onClick={VerLugares}>Ver lugares</Button>
        </Col>
        <Col>
          <Button onClick={NuevoLugar}>Nuevo</Button>
        </Col>
      </Row>  
      {mostrarLugares && (
        <Row className="d-flex justify-content-center">
          <Col xs={12} md={8} lg={6}>
            <TarjetaLugar lugares={lugares} />
          </Col>
        </Row>
      )}
      {mostrarFormulario && (
        <Row className="d-flex justify-content-center">
          <Col xs={12} md={8} lg={6}>
            <FormularioLugar onAgregarLugar={agregarLugar} />
          </Col>
        </Row>
      )}
    </Container>
  );
};

export default Album;
