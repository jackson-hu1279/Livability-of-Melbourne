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
import React from "react";
// reactstrap components
import { Card, CardHeader, CardBody, Row, Col } from "reactstrap";
// core components

function Home() {
  return (
    <>
      <div className="content">
        <Row>
          <Col md="12">
            <Card>
              <CardHeader>
                <center>
                  <h4 className="title" centre="true">
                    Cluster and Cloud Computing Assignment 2 (Team 53)
                  </h4>
                </center>
              </CardHeader>
              <CardBody>
                <center>
                  <p>
                    Our team came up with 2 main scenarios based on crime,
                    mental health and income of people living in Greater
                    Melbourne.
                  </p>
                  <p>
                    The data are collected and analysed in order to create
                    correlation between AURIN data and twitter data. In this
                    case, we aim to find out the livability of Greater Melbourne
                    in each Local Government Area (LGA) by comparing AURIN data
                    with the actual data posted on twitter by the locals.
                  </p>
                </center>
              </CardBody>
            </Card>

            <Card>
              <CardHeader>
                <center>
                  <h5 className="title" centre="true">
                    Scenario A
                  </h5>
                </center>
              </CardHeader>
              <CardBody>
                <center>
                  <p>
                    This scenario is based on crime data from Australian Urban
                    Research Infrastructure Network (AURIN) and tweets with
                    relevant keywords in Greater Melbourne.
                  </p>
                  <p className="blockquote blockquote">
                    Keywords: abduction abuse, accident, arson, assassination,
                    assault, bigamy, blackmail ,bombing ,bribery, burglary
                    ,corruption, crime,cybercrime, domestic violence, drug,
                    embezzlement, espionage, family violence, felony, forgery,
                    fraud, gang, genocide, hijacking, hit and run, homicide,
                    hooliganism ,identity theft, incident
                  </p>
                </center>
              </CardBody>
            </Card>

            <Card>
              <CardHeader>
                <center>
                  <h5 className="title" centre="true">
                    Scenario B
                  </h5>
                </center>
              </CardHeader>
              <CardBody>
                <center>
                  <p>
                    This scenario is based on the mental health and income data
                    from Australian Urban Research Infrastructure Network
                    (AURIN) and tweets with relevant keywords in Greater
                    Melbourne.
                  </p>
                  <p className="blockquote blockquote">
                    Keywords: anxiety, craziness, delusion, depression,
                    disturbed mind, dying, emotional disorder, emotional
                    instability, exhausted, hallucination, insanity, mental
                    disorder, mental disease, mental sickness, mental health,
                    nervous disorder, neurosis, neurotic disorder, personality
                    disorder, schizophrenia, self-harm, self harm, suicide
                  </p>
                </center>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </div>
    </>
  );
}

export default Home;
