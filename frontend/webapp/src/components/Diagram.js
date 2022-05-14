// # ----------------------------------------------
// # --------
// #
// # Cluster and Cloud Computing Assignment 2 - Team 53
// # 
// # Authors: 
// # - Chi Yin Wong (Student ID: 836872)
// # - Kaiquan Lin (Student ID: 1147233)
// # - Renkai Liao (Student ID: 1141584)
// # - Renwei Hu (Student ID: 1067974)
// # - Siwat Chairattanamanokorn (Student ID: 1338152)
// #
// # Author of this file:
// # - Siwat Chairattanamanokorn (Student ID: 1338152)
// #
// # Location:
// # - Melbourne
// #
// # --------
// # ----------------------------------------------

import React from "react";
import fetch from "node-fetch";
import BarChart from "./BarChart";

export default class Diagram extends React.Component {
  constructor(props) {
    super(props);
    var barChartData;

    this.state = {
      loading: true,
      title: props.title,
      url: props.data,
      barChartData: barChartData,
    };
  }

  UNSAFE_componentWillUpdate() {
    console.log(this.state.url);
    if (this.state.loading) {
      fetch(this.state.url, {
        headers: new Headers({
          Authorization: "Basic " + btoa("admin:admin"),
          "Content-Type": "application/json",
        }),
      })
        .then(function (response) {
          if (response.status >= 400) {
            alert("Error!!!" + response.status);
            throw new Error("Error!!!");
          }
          return response.json();
        })
        .then((data) => {
          console.log(data.rows);
          this.setState({
            loading: false,
            barChartData: data.rows,
          });
        });
    }
  }

  componentDidMount() {
    console.log(this.state.url);
    if (this.state.loading) {
      fetch(this.state.url, {
        headers: new Headers({
          Authorization: "Basic " + btoa("admin:admin"),
          "Content-Type": "application/json",
        }),
      })
        .then(function (response) {
          if (response.status >= 400) {
            alert("Error!!!" + response.status);
            throw new Error("Error!!!");
          }
          return response.json();
        })
        .then((data) => {
          this.setState({
            loading: false,
            barChartData: data.rows,
          });
        });
    }
  }

  render() {
    return this.state.loading ? (
      "loading"
    ) : (
      <BarChart data={this.state.barChartData} title={this.state.title} />
    );
  }
}
