/*!

=========================================================
* Paper Dashboard React - v1.3.0
=========================================================

* Product Page: https://www.creative-tim.com/product/paper-dashboard-react
* Copyright 2021 Creative Tim (https://www.creative-tim.com)

* Licensed under MIT (https://github.com/creativetimofficial/paper-dashboard-react/blob/main/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import KeplerMapDistress from "components/KeplerMapDistress";
import KeplerMapIncome from "components/KeplerMapIncome";
import React from "react";
// reactstrap components
import { Card, CardHeader, CardBody, Row, Col } from "reactstrap";

function ScenarioB() {
  return (
    <>
      <div className="content">
        <Row>
          <Col md="12">
            <Card>
              <CardHeader>
                <center>
                  <h5 className="title" centre>
                    Map Representation
                  </h5>
                </center>
              </CardHeader>
            </Card>

            <Card>
              <CardHeader>
                <h6>Distress Rate with Historic Mental Health Tweets</h6>
              </CardHeader>
              <CardBody>
                <div
                  id="map"
                  className="map"
                  style={{ position: "relative", overflow: "hidden" }}
                >
                  <p>
                    Distress rate data in each Greater Melbourne LGA collected
                    from AURIN is plotted as a heatmap with historic mental
                    health tweets displays in a cluster format.
                  </p>
                  <KeplerMapDistress />
                </div>
              </CardBody>
            </Card>

            <Card>
              <CardHeader>
                <h6>Income with Historic Mental Health Tweets</h6>
              </CardHeader>
              <CardBody>
                <div
                  id="map"
                  className="map"
                  style={{ position: "relative", overflow: "hidden" }}
                >
                  <p>
                    Income data in each Greater Melbourne LGA collected from
                    AURIN is plotted as a heatmap with historic mental health
                    tweets displays in a cluster format.
                  </p>
                  <KeplerMapIncome />
                </div>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </div>
    </>
  );
}

export default ScenarioB;
