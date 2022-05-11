import React from "react";
import fetch from "node-fetch";
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
      url: props.data,
      pieChartData: pieChartData,
      barChartData: barChartData,
    };
  }

  UNSAFE_componentWillUpdate() {
    console.log(this.state.url);
    fetch(this.state.url, {
      headers: new Headers({
        Authorization: "Basic " + btoa("admin:admin"),
        "Content-Type": "application/json",
      }),
    })
      .then(function (res) {
        if (res.status >= 400) {
          alert("Bad response from server: " + res.status);
          throw new Error("Bad response from server");
        }
        return res.text();
      })
      .then((data) => {
        console.log(data);
        this.setState({
          isLoading: false,
        });
      })
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

  componentDidMount() {
    console.log(this.state.url);
    fetch(this.state.url, {
      headers: new Headers({
        Authorization: "Basic " + btoa("admin:admin"),
        "Content-Type": "application/json",
      }),
    })
      .then(function (res) {
        if (res.status >= 400) {
          alert("Bad response from server: " + res.status);
          throw new Error("Bad response from server");
        }
        return res.text();
      })
      .then((data) => {
        console.log(data);
        this.setState({
          isLoading: false,
        });
      })
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
