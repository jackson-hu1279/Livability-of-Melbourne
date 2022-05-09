import React from "react";
import fetch from "fetch-with-proxy";

import { Grid, Row, Col, Panel } from "rsuite";
import PieChart from "./PieChart";
import BarChart from "./BarChart";

export default class Diagram extends React.Component {
  constructor(props) {
    super(props);
    var pieChartData;
    var barChartData;

    this.state = {
      isLoading: true,
      url: "http://172.26.134.126:5984/_utils/#/database/crime_historical/_design/LGA_COUNT/_view/count-lga-name-code",
      pieChartData: pieChartData,
      barChartData: barChartData,
    };
  }

  UNSAFE_componentWillUpdate(nextProps, nextState) {
    console.log(nextProps);
    var pieChartData;
    var barChartData;

    if (nextProps.data !== this.state.url) {
      this.state.url = nextProps.data;
      fetch(this.state.url)
        .then(function (res) {
          if (res.status >= 400) {
            alert("Bad response from server: " + res.status);
            throw new Error("Bad response from server");
          }
          return res.json();
        })
        .then((data) => {
          // console.log(data);
          // pieChartData = data.pie_charts_for_each_city_all_age_groups.pieChart;
          // barChartData = data.barChart_total_pop;
          // this.setState({
          //   pieChartData: pieChartData,
          //   barChartData: barChartData,
          //   isLoading: false,
          // });
          // console.log(this.state.muitiBarChartData1);
        })
        .then(
          (res) => {
            if (res.ok) {
              console.log("ok");
            } else {
              console.log("error");
            }
            console.log(res.json());
          },
          (err) => {
            console.log(err);
          }
        )
        .then(
          (data) => {
            console.log(data);
          },
          (err) => {
            console.log(err);
          }
        );
    }
  }

  componentDidMount() {
    var pieChartData;
    var barChartData;
    fetch(this.state.url)
      .then(function (res) {
        if (res.status >= 400) {
          alert("Bad response from server: " + res.status);
          throw new Error("Bad response from server");
        }
        return res.json();
      })
      .then((data) => {
        console.log(data);
        pieChartData = data.pie_charts_for_each_city_all_age_groups.pieChart;
        barChartData = data.barChart_total_pop;
        this.setState({
          pieChartData: pieChartData,
          barChartData: barChartData,
          isLoading: false,
        });
        console.log(this.state.muitiBarChartData1);
      })
      .then(
        (res) => {
          if (res.ok) {
            console.log("ok");
          } else {
            console.log("error");
          }
          console.log(res.json());
        },
        (err) => {
          console.log(err);
        }
      )
      .then(
        (data) => {
          console.log(data);
        },
        (err) => {
          console.log(err);
        }
      );
  }

  render() {
    return this.state.isLoading ? (
      "loading"
    ) : (
      <Grid fluid width={window.innerWidth} height={window.innerHeight}>
        <Row className="show-grid" gutter={30}>
          {this.state.barChartData.map((item) => {
            return (
              <Col md={12} sm={12}>
                <Panel shaded bordered expanded>
                  <BarChart data={item} title="Total Population" />
                </Panel>
              </Col>
            );
          })}
          {
            <Col md={12} sm={12}>
              <Panel shaded bordered expanded></Panel>
            </Col>
          }
        </Row>

        <Row className="show-grid" gutter={30}>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded></Panel>
          </Col>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded></Panel>
          </Col>
        </Row>
        <Row className="show-grid" gutter={30}>
          {this.state.pieChartData.map((item) => {
            return (
              <Col md={12} sm={12}>
                <Panel shaded bordered expanded>
                  <PieChart data={item} />
                </Panel>
              </Col>
            );
          })}
        </Row>
      </Grid>
    );
  }
}
