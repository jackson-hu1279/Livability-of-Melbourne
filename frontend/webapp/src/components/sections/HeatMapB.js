import React from "react";
import KeplerMapDistress from "../KeplerMapDistress";
import KeplerMapIncome from "../KeplerMapIncome";

const HeatMapB = () => {
  return (
    <section>
      <div className="container">
        <div>
          <div>
            <div className="text-xxs text-color-primary fw-600 tt-u mb-8">
              AURIN DATA
            </div>
            <h3 className="mt-0 mb-12">Distress Rate</h3>
            <p className="m-0">
              The heatmap is displaying the distress rate of people living in
              each Greater Melbourne LGA
            </p>
            <div class="centre"></div>
            <KeplerMapDistress />
          </div>
        </div>
      </div>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <br></br>
      <div className="container">
        <div>
          <div>
            <div className="text-xxs text-color-primary fw-600 tt-u mb-8">
              AURIN DATA
            </div>
            <h3 className="mt-0 mb-12">Average Income</h3>
            <p className="m-0">
              The heatmap is displaying the information according to the average
              income of people living in each Greater Melbourne LGA
            </p>
            <div class="centre">
              <KeplerMapIncome />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeatMapB;
