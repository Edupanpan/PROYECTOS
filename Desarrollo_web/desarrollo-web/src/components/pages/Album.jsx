import React, { useState, useEffect } from 'react';
import { Container, Row, Col, DropdownButton, Dropdown, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Album.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import TarjetaLugar from '../tarjetalugar';
import ModalLugar from '../modal'; // Importar el nuevo componente ModalLugar

const Album = () => {
  const navigate = useNavigate();//hook para navegar entre rutas

  const [lugares, setLugares] = useState([]);//definicion de un estado y una funcion para actualizarlo
  
  // Función para obtener los datos de MockAPI
  const obtenerDatos = async () => {
    const response = await axios.get('https://66fd61c7699369308954fd8e.mockapi.io/lugares/visita');
    setLugares(response.data);
  };

  useEffect(() => {
    obtenerDatos();
  }, []);
  
  const agregarLugar = async (nuevoLugar) => {
    // Realiza la petición POST a la API
    const respuesta = await axios.post('https://66fd61c7699369308954fd8e.mockapi.io/lugares/visita', nuevoLugar);
    setLugares((prevLugares) => [...prevLugares, respuesta.data]); // Agrega el nuevo lugar a la lista
    setMostrarModal(false); // Cierra el modal
  };
  
  const [lugarSeleccionado, setLugarSeleccionado] = useState(null); // Estado para el lugar seleccionado
  const [isEditing, setIsEditing] = useState(false); // Estado para el modo de edición
  
  const actualizarLugar = async (lugarActualizado) => {
    // Realiza la petición PUT a la API
    const respuesta = await axios.put(`https://66fd61c7699369308954fd8e.mockapi.io/lugares/visita/${lugarActualizado.id}`, lugarActualizado);
    
    if (respuesta.status === 200) {
      // Actualiza el estado local con los datos actualizados
      setLugares((prevLugares) =>
        prevLugares.map((lugar) =>
          lugar.id === lugarActualizado.id ? respuesta.data : lugar
        )
      );
      setMostrarModal(false); // Cierra el modal
    } else {
      console.error('Error al actualizar el lugar en MockAPI');
    }
  };

  const eliminarLugar = async (id) => {
    await axios.delete(`https://66fd61c7699369308954fd8e.mockapi.io/lugares/visita/${id}`);
    setLugares((prevLugares) => prevLugares.filter((lugar) => lugar.id !== id));
  };

  const [mostrarModal, setMostrarModal] = useState(false); // Estado para controlar el modal
  function handleModal() {
    setMostrarModal(!mostrarModal);
  }
  const editarLugar = (lugar) => {
    setLugarSeleccionado(lugar);
    setIsEditing(true);
    setMostrarModal(true);
  };

  return (
    <Container className="d-flex flex-column vh-100 align-items-center">
      <Row className="m-4 w-100 d-flex align-items-center justify-content-center">
        <Col xs={2} className="text-start">
          <DropdownButton variant='dark' id="bg-nested-dropdown" title="Opciones">
            <Dropdown.Item eventKey="1" onClick={() => navigate('/')}>
              Home
            </Dropdown.Item>
            <Dropdown.Item eventKey="2" onClick={() => { setIsEditing(false); setLugarSeleccionado(null); handleModal(); }}>
              Nuevo
            </Dropdown.Item>
            <Dropdown.Item eventKey="2" onClick={()=>navigate('/Mapa')}>
              Ver Mapa
            </Dropdown.Item>
          </DropdownButton>
        </Col>
        <Col className="text-center">
          <h1 className="display-4">Mis Lugares</h1>
        </Col>
        <Col xs={2} className="text-end">
          <p>Eduardo Silva</p>
        </Col>
      </Row>
      <Row className="d-flex justify-content-center w-100">
        <Col>
          <TarjetaLugar lugares={lugares} editarLugar={editarLugar} eliminarLugar={eliminarLugar} />
        </Col>
      </Row>
      <ModalLugar
        mostrarModal={mostrarModal}
        handleModal={handleModal}
        agregarLugar={agregarLugar}
        lugar={lugarSeleccionado}
        isEditing={isEditing}
        actualizarLugar={actualizarLugar}
      />
    </Container>
  );
};

export default Album;