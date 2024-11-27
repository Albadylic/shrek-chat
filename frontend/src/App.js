import React, { useState } from "react";

import { ReactComponent as Shrek } from "./shrek.svg";

{
  /* <a target="_blank" href="https://icons8.com/icon/26BhkJZRzRCR/shrek">Shrek</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a> */
}

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();
    try {
      const res = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error("Error:", error);
      setResponse("An error occurred.");
    }
    setLoading(false);
  };

  return (
    <div className="App h-screen flex  flex-col items-center justify-center bg-lime-800">
      <div className="flex flex-col items-center justify-center bg-stone-400/70	rounded p-5 my-2 min-w-96">
        <h1 className="text-3xl font-semibold my-3">Ask Shrek</h1>
        <form
          onSubmit={handleSubmit}
          className="text-l my-2 flex justify-center"
        >
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask your question..."
            className="p-2 mx-1 rounded"
          />
          <button
            type="submit"
            className="p-2 mx-1 bg-lime-950	text-white rounded max-h-32"
            disabled={loading}
          >
            Submit
          </button>
        </form>
      </div>
      <div className="flex flex-col items-center justify-center bg-stone-400/70	rounded p-5 m-2">
        {loading ? (
          <Shrek className="animate-pulse" />
        ) : (
          <p>{response.response || "Response will generate here"}</p>
        )}
      </div>
    </div>
  );
}

export default App;
