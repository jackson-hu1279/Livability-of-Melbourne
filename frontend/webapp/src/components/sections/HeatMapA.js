import React from "react";
import KeplerMapDrug from "../KeplerMapDrug";
import KeplerMapViolence from "../KeplerMapViolence";

const HeatMapA = () => {
  return (
    <section>
      <div className="container">
        <div>
          <div>
            <div className="text-xxs text-color-primary fw-600 tt-u mb-8">
              AURIN DATA
            </div>
            <h3 className="mt-0 mb-12">Family Violence</h3>
            <p className="m-0">
              The heatmap is displaying the rate of family violence per 1000
              population in each Greater Melbourne LGA
            </p>
            <div class="centre"></div>
            <KeplerMapViolence />
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
            <h3 className="mt-0 mb-12">Drug Use</h3>
            <p className="m-0">
              The heatmap is displaying the rate of drug use per 1000 population
              in each Greater Melbourne LGA
            </p>
            <div class="centre">
              <KeplerMapDrug />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeatMapA;
