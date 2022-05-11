import CanvasJSReact from "../assets/canvasJS/canvasjs.react";
import React from "react";

var CanvasJSChart = CanvasJSReact.CanvasJSChart;

export default class BarChart extends React.Component {
  constructor(props) {
    super(props);
    var datas = [];
    var data = props.data;
    this.state = {
      title: props.title,
      data: data,
      points: datas,
    };

    console.log(data);
    for (var i = 0; i < data.length; i++) {
      console.log(data[i].key["LGA_NAME"]);
      console.log(data[i].value);
      datas.push({
        label: data[i].key["LGA_NAME"],
        y: data[i].value,
      });
    }
    console.log(datas);
  }

  render() {
    const options = {
      title: {
        text: this.state.title,
      },
      axisX: {
        valueFormatString: "string",
      },
      data: [
        {
          type: "column",
          xValueFormatString: "string",
          yValueFormatString: "###",
          dataPoints: this.state.points,
        },
      ],
    };

    return (
      <CanvasJSChart
        options={options}
        onRef={(ref) => (this.chart = ref)}
        style={{ width: 100 }}
      />
    );
  }
}
