import React from "react";

interface Props {
  chatbotMessage: string[];
  userMessage: string[];
}

export default class Chat extends React.Component<Props> {
  render() {
    return (
      <div className="bg-red-500 w-11/12 ml-[4%] mt-2">
        <h1>Chat</h1>
      </div>
    );
  }
}
