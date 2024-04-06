import React from "react";

interface Props {
  onNewUserQuestion: any;
  onNewChatbotAnswer: any;
}

interface State {
  question: string;
}
export default class UserInput extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.state = {
      question: "",
    };
  }
  private handleChange(e) {
    this.setState({ question: e.target.value });
  }
  private handleClick() {
    this.props.onNewUserQuestion(this.state.question);
    this.setState({ question: "" });
    this.props.onNewChatbotAnswer("lorem lorem lorem lorem");
  }
  render() {
    const question: string = this.state.question;
    return (
      <div className=" flex border-2 border-indigo-400 rounded-lg w-11/12 ml-[4%]">
        <input
          className="text-black placeholder:italic w-11/12 border-slate-300 rounded-md py-2 pl-4 pr-3 focus:outline-none focus:border-indigo-400 sm:text-sm"
          placeholder="Ask me something ..."
          type="text"
          name="askQuestion"
          value={question}
          onChange={this.handleChange}
        />
        <div className="w-1/12 flex md:justify-end md:me-3">
          <i
            className="fi fi-br-paper-plane-top text-black text-2xl mt-1.5 hover:cursor-pointer"
            onClick={this.handleClick}
          />
        </div>
      </div>
    );
  }
}
