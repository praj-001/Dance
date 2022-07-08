import "./transcript.css";
import axios from "axios";
import { useState } from "react";

export default function Transcript() {
  const [transcript, setTranscript] = useState([]);
  let handleTranscript = async () => {
    let res = await axios.get("http://localhost:4000/api/corpus");
    console.log(res.data.output);
    setTranscript(res.data.output);
  };
  return (
    <>
      <div className="transcript-content">
        <div className="box1">
          <h3> Meetings</h3>
          <li>Meeting 1</li>
          <li>Meeting 2</li>
          <li>Meeting 3</li>
        </div>
        <div className="box2">
          <h3> Transcription</h3>
          <button onClick={() => handleTranscript()}>Get transcript</button>
          <div className="output">
            {transcript.map((line, key) => {
              return (<div key={key}>{line}</div>)
            })}
          </div>
        </div>
        <div className="box3">
          <p> Number of Speakers</p>
        </div>
      </div>
      <div className="box4">
        <button> Get Recording</button>
      </div>
    </>
  );
}
