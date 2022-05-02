import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap";

const NavBar = () => {
  return (
    <Navbar bg="primary" variant="dark">
      <Container>
        <Navbar.Brand href="/">Home</Navbar.Brand>
        <Nav className="me-auto">
          <Nav.Link href="/distress">Distress</Nav.Link>
          <Nav.Link href="/drug">Drug</Nav.Link>
          <Nav.Link href="/family_violence">Family Violence</Nav.Link>
          <Nav.Link href="/income">Income</Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
};
export default NavBar;
