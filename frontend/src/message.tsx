import React from "react";

interface Props {
  messageContent: string;
  state: string;
}

export default class Message extends React.Component<Props, {}> {
  render() {
    return this.props.state === "user" ? (
      <div className="flex justify-end">
        <div className="w-5/12 bg-yellow-300">
          <p>{this.props.messageContent}</p>
        </div>
      </div>
    ) : (
      <div className="flex justify-start">
        <div className="w-5/12 bg-green-800">
          <p>{this.props.messageContent}</p>
        </div>
      </div>
    );
  }
}
