import React from "react";
import Message from "./message";
interface Props {
  chatbotMessage: string[];
  userMessage: string[];
}

export default class Chat extends React.Component<Props, {}> {
  render() {
    return (
      <div className="w-11/12 ml-[4%] mt-2">
        {this.props.chatbotMessage.map((value, index) => {
          return [
            <Message
              messageContent={this.props.userMessage[index]}
              state={"user"}
            />,
            <Message messageContent={value} state={"chatbot"} />,
          ];
        })}
      </div>
    );
  }
}
