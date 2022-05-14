/*!

=========================================================
* Paper Dashboard React - v1.3.0
=========================================================

* Product Page: https://www.creative-tim.com/product/paper-dashboard-react
* Copyright 2021 Creative Tim (https://www.creative-tim.com)

* Licensed under MIT (https://github.com/creativetimofficial/paper-dashboard-react/blob/main/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# ----------------------------------------------
# --------
#
# Cluster and Cloud Computing Assignment 2 - Team 53
# 
# Authors: 
# - Chi Yin Wong (Student ID: 836872)
# - Kaiquan Lin (Student ID: 1147233)
# - Renkai Liao (Student ID: 1141584)
# - Renwei Hu (Student ID: 1067974)
# - Siwat Chairattanamanokorn (Student ID: 1338152)
#
# Author of this file:
# - Siwat Chairattanamanokorn (Student ID: 1338152)
#
# Location:
# - Melbourne
#
# --------
# ----------------------------------------------
*/
import Home from "views/Home.js";
import ScenarioA from "views/ScenarioA";
import ScenarioB from "views/ScenarioB";

var routes = [
  {
    path: "/home",
    name: "Home",
    icon: "nc-icon nc-bank",
    component: Home,
    layout: "/CCC",
  },
  {
    path: "/scenario_a",
    name: "Scenario A",
    icon: "nc-icon nc-credit-card",
    component: ScenarioA,
    layout: "/CCC",
  },
  {
    path: "/scenario_b",
    name: "Scenario B",
    icon: "nc-icon nc-credit-card",
    component: ScenarioB,
    layout: "/CCC",
  },
];
export default routes;
