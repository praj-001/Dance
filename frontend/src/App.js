import Navbar from "./Navbar"
import Home from "./pages/Home"
import Transcript from "./pages/Transcript"
import { Route, Routes } from "react-router-dom"

function App() {
  return (
    <>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/transcript" element={<Transcript />} />
        </Routes>
      </div>
    </>
  )
}

export default App