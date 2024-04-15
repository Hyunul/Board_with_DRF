import './App.css';
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import Test from './components/Test';
import Post from './components/BoardList';
import BoardDetail from './components/BoardDetail';

function App() {
  return (
    <Router>
      <Link to="/Test/">Test</Link>
      <Link to="/post/">Post</Link>
      <Routes>
        <Route path="/Test/" element={<Test />} />
        <Route path="/post/" element={<Post />} />
        <Route path="/post/:id/" element={<BoardDetail />} />
      </Routes>
    </Router>
  );
}

export default App;