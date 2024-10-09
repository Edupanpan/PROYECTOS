import React from 'react';
import './Navbar.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { useNavigate } from 'react-router-dom';

const CustomNavbar = () => {
  const navigate = useNavigate();

  const toalbum = () => {
    navigate('/album');
  };

  const tohome = () => {
    navigate('/');
  };

  return (
    <Navbar expand="lg" className='nav'>
      <Container>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mx-auto">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="nav-link" onClick={tohome}>Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" onClick={toalbum}>Album</a>
              </li>
            </ul>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default CustomNavbar;