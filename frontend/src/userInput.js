import React from "react";

export default class UserInput extends React.Component {
  render() {
    return (
      <div className=" flex  border-2 border-indigo-400 rounded-lg w-11/12 ml-[4%]">
        <input
          className="text-black placeholder:italic w-11/12 border-slate-300 rounded-md py-2 pl-4 pr-3 focus:outline-none focus:border-indigo-400 sm:text-sm"
          placeholder="Ask me something ..."
          type="text"
          name="search"
        />
        <div className="w-1/12 flex md:justify-end md:me-3">
          <i className="fi fi-br-paper-plane-top text-black text-2xl mt-1.5 hover:cursor-pointer"></i>
        </div>
      </div>
    );
  }
}
