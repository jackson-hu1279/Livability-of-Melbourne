import { PieChart } from "react-minimal-pie-chart";
import axios from "axios";
axios.get("http://172.26.134.126:5984").then((json) => console.log(json));

export default function PieChartCrimeTwitter() {
  return (
    <PieChart
      data={[
        { title: "One", value: 10, color: "#E38627" },
        { title: "Two", value: 15, color: "#C13C37" },
        { title: "Three", value: 20, color: "#6A2135" },
      ]}
    />
  );
}
