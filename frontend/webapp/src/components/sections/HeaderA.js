import React from "react";
import SectionHeader from "./partials/SectionHeader";

const HeaderA = () => {
  const sectionHeader = {
    title: "Scenario A",
    paragraph:
      "The focus of this scenario is based on the crime rate (drug use and family violence) of Greater Melbourne LGA",
  };

  return <SectionHeader data={sectionHeader} className="center-content" />;
};

export default HeaderA;
