import './App.css';
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import Test from './components/Test';
import Example from './components/Reponsive';
import { renderLineChart } from './components/Chart';

function App() {
  return (
    <div>
      {/* <Router>
        <Link to="/Test/">Test</Link>
        <Routes>
          <Route path="/Test/" element={<Test />} />
        </Routes>
      </Router> */}
      <Example />
      <renderLineChart />

    </div>
  );
}

export default App;

