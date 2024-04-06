import React from "react";

export default class Header extends React.Component {
  render() {
    return (
      <div className="bg-gradient-to-r from-indigo-400 to-indigo-300 min-h-12 flex flex-row items-center justify-between text-xl md:rounded-t-[0.35rem]">
        <div className="flex justify-around w-header">
          <i className="fi fi-rr-chatbot-speech-bubble text-2xl"></i>
          <h1 className="italic font-bold">Gastronomy Chatbot</h1>
        </div>
        <div className="w-20 flex justify-around">
          <i className="fi fi-rr-refresh hover:cursor-pointer"></i>
          <i className="fi fi-br-cross hover:cursor-pointer"></i>
        </div>
      </div>
    );
  }
}
