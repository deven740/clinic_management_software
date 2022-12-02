import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LogIn from "./components/login/login";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/login" element={<LogIn />} />
          <Route path="/" element={<LogIn />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
