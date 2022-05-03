import React from "react";
import { Navbar, Container, Nav, NavDropdown } from "react-bootstrap";

const NavBar = () => {
  return (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
      <Container>
        <Navbar.Brand href="/">Home</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto">
            <NavDropdown title="Scenario A" id="collasible-nav-dropdown">
              <NavDropdown.Item href="/scenario_a_aurin">
                Aurin
              </NavDropdown.Item>
              <NavDropdown.Item href="/scenario_a_twitter">
                Twitter
              </NavDropdown.Item>
            </NavDropdown>

            <NavDropdown title="Scenario B" id="collasible-nav-dropdown">
              <NavDropdown.Item href="/scenario_b_aurin">
                Aurin
              </NavDropdown.Item>
              <NavDropdown.Item href="/scenario_b_twitter">
                Twitter
              </NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;
