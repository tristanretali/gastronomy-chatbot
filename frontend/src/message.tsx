import React from "react";

interface Props {
  messageContent: string;
  state: string;
}

export default class Message extends React.Component<Props, {}> {
  render() {
    return this.props.state === "user" ? (
      <div className="flex justify-end">
        <div className="w-5/12 border border-blue-400 rounded-md text-black ps-2.5">
          <p>{this.props.messageContent}</p>
        </div>
      </div>
    ) : (
      <div className="flex justify-start">
        <div className="w-5/12 bg-blue-400 ps-2.5 rounded-md">
          <p>{this.props.messageContent}</p>
        </div>
      </div>
    );
  }
}
