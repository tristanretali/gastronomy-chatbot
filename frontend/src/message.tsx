import React from "react";

interface Props {
  messageContent: string;
  state: string;
}

export default class Message extends React.Component<Props, {}> {
  render() {
    return this.props.state === "user" ? <div></div> : <div></div>;
  }
}
