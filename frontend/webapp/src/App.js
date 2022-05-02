import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Distress from "./pages/Distress";
import Drug from "./pages/Drug";
import FamilyViolence from "./pages/FamilyViolence";
import Income from "./pages/Income";
import Home from "./pages/Home";

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/distress" element={<Distress />} />
        <Route path="/drug" element={<Drug />} />
        <Route path="/family_violence" element={<FamilyViolence />} />
        <Route path="/income" element={<Income />} />
      </Routes>
    </Router>
  );
}

export default App;
