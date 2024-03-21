import Chatbot from "./chatbot";
import React from "react";

function App() {

    return (
    <div className="min-w-full min-h-screen bg-neutral-600 text-center">
        <main className="container bg-green-800 min-h-screen flex flex-col justify-center items-center">
            <Chatbot/>
        </main>
    </div>
  );
}

export default App;
