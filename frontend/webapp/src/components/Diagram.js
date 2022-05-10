import React from "react";
import fetch from "fetch-with-proxy";
import crime_data from "../data/testData/historicTwitter/crime-tweet-count.json";
import mental_data from "../data/testData/historicTwitter/mental-tweet-count.json";

import { Grid, Row, Col, Panel } from "rsuite";

export default class Diagram extends React.Component {
  constructor(props) {
    super(props);
    var pieChartData;
    var barChartData;

    this.state = {
      isLoading: true,
      pieChartData: pieChartData,
      barChartData: barChartData,
    };
  }

  UNSAFE_componentWillUpdate() {
    fetch(
      "http://172.26.134.126:5984/crime_historical/_design/LGA_COUNT/_view/COUNT?reduce=true&group_level=1",
      {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      }
    )
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

  componentDidMount() {
    fetch(
      "http://172.26.134.126:5984/crime_historical/_design/LGA_COUNT/_view/COUNT?reduce=true&group_level=1"
    )
      .then(
        (res) => {
          if (res.ok) {
            console.log("ok");
          } else {
            console.log("error");
          }
          console.log(res.text());
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
      <Grid fluid width={window.innerWidth} height={window.innerHeight}></Grid>
    );
  }
}
