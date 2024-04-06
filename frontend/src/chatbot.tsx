import React from "react";
import Header from "./header";
import Chat from "./chat";
import UserInput from "./userInput";
interface State {
  chatbotMessage: string[];
  userMessage: string[];
}
export default class Chatbot extends React.Component<{}, State> {
  constructor(props: any) {
    super(props);
    this.state = {
      chatbotMessage: [],
      userMessage: [],
    };
  }

  render() {
    const chatbotMessage: string[] = this.state.chatbotMessage;
    const userMessage: string[] = this.state.userMessage;
    return (
      <div className="w-full flex flex-col min-h-screen justify-between pb-6 text-white md:min-h-desktop md:border-solid md:border-2 md:border-cyan-500 md:rounded-lg md:w-11/12 md:mt-6 ">
        <div>
          <Header />
          <Chat chatbotMessage={chatbotMessage} userMessage={userMessage} />
        </div>
        <UserInput />
      </div>
    );
  }
}
