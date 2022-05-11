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
