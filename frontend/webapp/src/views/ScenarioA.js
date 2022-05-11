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
import Diagram from "components/Diagram";
import KeplerMapDrug from "components/KeplerMapDrug";
import KeplerMapViolence from "components/KeplerMapViolence";
import React from "react";
// reactstrap components
import { Card, CardHeader, CardBody, Row, Col } from "reactstrap";

const url =
  "http://172.26.134.126:5984/crime_historical/_design/LGA_COUNT/_view/count-lga-name-code?reduce=true&group_level=1";

function ScenarioA() {
  return (
    <>
      <div className="content">
        <Row>
          <Col md="12">
            <Card>
              <CardHeader>
                <center>
                  <h5 className="title" centre="true">
                    AURIN
                  </h5>
                </center>
              </CardHeader>
            </Card>

            <Card>
              <CardHeader>
                <h6>
                  Number of crime related tweets in each Local Government Area
                </h6>
              </CardHeader>
              <CardBody>
                <div
                  id="map"
                  className="map"
                  style={{ position: "relative", overflow: "hidden" }}
                >
                  <Diagram data={url} />
                </div>
              </CardBody>
            </Card>

            <Card>
              <CardHeader>
                <center>
                  <h5 className="title" centre="true">
                    Map Representation
                  </h5>
                </center>
              </CardHeader>
            </Card>

            <Card>
              <CardHeader>
                <h6>Family Violence with Historic Crime Tweets</h6>
              </CardHeader>
              <CardBody>
                <div
                  id="map"
                  className="map"
                  style={{ position: "relative", overflow: "hidden" }}
                >
                  <p>
                    Family Violence data in each Greater Melbourne LGA collected
                    from AURIN is plotted as a heatmap with historic crime
                    tweets displays in a cluster format.
                  </p>
                  <KeplerMapViolence />
                </div>
              </CardBody>
            </Card>

            <Card>
              <CardHeader>
                <h6>Drug use with Historic Crime Tweets</h6>
              </CardHeader>
              <CardBody>
                <div
                  id="map"
                  className="map"
                  style={{ position: "relative", overflow: "hidden" }}
                >
                  <p>
                    Drug use data in each Greater Melbourne LGA collected from
                    AURIN is plotted as a heatmap with historic crime tweets
                    displays in a cluster format.
                  </p>
                  <KeplerMapDrug />
                </div>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </div>
    </>
  );
}

export default ScenarioA;
