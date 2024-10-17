import React from 'react';
import { Modal, Button } from 'react-bootstrap';
import FormularioLugar from './formulariolugar'; // Ruta corregida

const ModalLugar = ({ mostrarModal, handleModal, agregarLugar, lugar, isEditing, actualizarLugar }) => {
  return (
    <Modal show={mostrarModal} onHide={handleModal}>
      <Modal.Header closeButton>
        <Modal.Title>{isEditing ? 'Editar lugar' : 'Agregar nuevo lugar'}</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <FormularioLugar 
          onAgregarLugar={agregarLugar} 
          lugar={lugar} // Pasa el lugar si está editando
          isEditing={isEditing} // Indica si es edición
          actualizarLugar={actualizarLugar} // Maneja la actualización del lugar
        />
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleModal}>
          Cerrar
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default ModalLugar;