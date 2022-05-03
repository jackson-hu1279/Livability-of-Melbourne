import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Home from "./pages/Home";
import ScenarioAAurin from "./pages/ScenarioAAurin";
import ScenarioBAurin from "./pages/ScenarioBAurin";

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/scenario_a_aurin" element={<ScenarioAAurin />} />
        <Route path="/scenario_b_aurin" element={<ScenarioBAurin />} />
        {/* <Route path="/scenario_b" element={<ScenarioA />} /> */}
      </Routes>
    </Router>
  );
}

export default App;
