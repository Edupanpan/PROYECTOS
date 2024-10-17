import React, { useState, useEffect } from 'react';
import { Container, Row, Col, DropdownButton, Dropdown } from 'react-bootstrap';
import './tarjetalugar.css';

const TarjetaLugar = ({ lugares, editarLugar, eliminarLugar }) => {
  // Al montar el componente, cargamos los lugares desde las props
  const [listaLugares, setListaLugares] = useState(lugares);

  useEffect(() => {
    setListaLugares(lugares);
    console.log('Lugares recibidos:', lugares); // Log para depuración
  }, [lugares]);

  return (
    <Container>
      <Row>
        {listaLugares.map((lugar) => (
            <Col key={lugar.id} xs={12} md={6} lg={3} className="mb-4">
              <div className="bg-white h-100 p-3">
                <Row className="d-flex justify-content-between align-items-center">
                  <Row xs="auto">
                    <DropdownButton
                      variant="link"
                      id={`dropdown-${lugar.id}`}
                      className="p-0"
                    >
                      <Dropdown.Item eventKey="1" onClick={() => editarLugar(lugar)}>
                        Editar
                      </Dropdown.Item>
                      <Dropdown.Item
                        eventKey="2"
                        onClick={() => eliminarLugar(lugar.id)}
                      >
                        Eliminar
                      </Dropdown.Item>
                    </DropdownButton>
                  </Row>
                  <Row xs="auto">
                    <h2 className="m-0 text-center">{lugar.nombre}</h2>
                  </Row>
                </Row>

                <Row className="text-center mt-3">
                  <Col>
                    <img
                      src={lugar.imagen}
                      alt={lugar.nombre}
                      className="img-fluid"
                    />
                  </Col>
                </Row>

                <Row className="text-center mt-2">
                  <Col>
                    <p>{lugar.fechavisita}</p>
                    <p>{lugar.direccion}</p>
                  </Col>
                </Row>
              </div>
            </Col>
          ))}
      </Row>
    </Container>
  );
};

export default TarjetaLugar;