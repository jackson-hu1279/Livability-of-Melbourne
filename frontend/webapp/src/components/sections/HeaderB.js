import React from "react";
import SectionHeader from "./partials/SectionHeader";

const HeaderB = () => {
  const sectionHeader = {
    title: "Scenario B",
    paragraph:
      "The focus of this scenario is based on the mental health and income of Greater Melbourne LGA",
  };

  return <SectionHeader data={sectionHeader} className="center-content" />;
};

export default HeaderB;
