import Chatbot from "./chatbot";
import React from "react";

function App() {
  return (
    <div className="min-w-full min-h-screen bg-neutral-600">
      <main className="container bg-white min-h-screen flex flex-col items-center">
        <Chatbot />
      </main>
    </div>
  );
}

export default App;
