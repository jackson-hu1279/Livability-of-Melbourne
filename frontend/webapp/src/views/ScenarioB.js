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

# ----------------------------------------------
# --------
#
# Cluster and Cloud Computing Assignment 2 - Team 53
# 
# Authors: 
# - Chi Yin Wong (Student ID: 836872)
# - Kaiquan Lin (Student ID: 1147233)
# - Renkai Liao (Student ID: 1141584)
# - Renwei Hu (Student ID: 1067974)
# - Siwat Chairattanamanokorn (Student ID: 1338152)
#
# Author of this file:
# - Siwat Chairattanamanokorn (Student ID: 1338152)
#
# Location:
# - Melbourne
#
# --------
# ----------------------------------------------
*/
import KeplerMapDistress from "components/KeplerMapDistress";
import KeplerMapIncome from "components/KeplerMapIncome";
import React from "react";
import Diagram from "components/Diagram";
// reactstrap components
import { Card, CardHeader, CardBody, Row, Col } from "reactstrap";

const url =
  "http://172.26.134.126:5984/mental_historical/_design/LGA_COUNT/_view/count-lga-name-code?reduce=true&group_level=1";

function ScenarioB() {
  return (
    <>
      <div className="content">
        <Row>
          <Col md="12">
            <Card>
              <CardHeader>
                <center>
                  <h5 className="title" centre="true">
                    Mental Health Tweets
                  </h5>
                </center>
              </CardHeader>
            </Card>

            <Card>
              <CardHeader>
                <h6>
                  Number of mental health related tweets in each Local
                  Government Area
                </h6>
              </CardHeader>
              <CardBody>
                <div
                  id="map"
                  className="map"
                  style={{ position: "relative", overflow: "hidden" }}
                >
                  <Diagram
                    data={url}
                    title={"No. of Mental Health Tweets in each LGA"}
                  />
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
                <h6>Distress Rate with Mental Health Tweets</h6>
              </CardHeader>
              <CardBody>
                <div
                  id="map"
                  className="map"
                  style={{ position: "relative", overflow: "hidden" }}
                >
                  <p>
                    Distress rate data in each Greater Melbourne LGA collected
                    from AURIN is plotted as a heatmap with mental health tweets
                    displays in a cluster format.
                  </p>
                  <KeplerMapDistress />
                </div>
              </CardBody>
            </Card>

            <Card>
              <CardHeader>
                <h6>Income with Mental Health Tweets</h6>
              </CardHeader>
              <CardBody>
                <div
                  id="map"
                  className="map"
                  style={{ position: "relative", overflow: "hidden" }}
                >
                  <p>
                    Income data in each Greater Melbourne LGA collected from
                    AURIN is plotted as a heatmap with mental health tweets
                    displays in a cluster format.
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
