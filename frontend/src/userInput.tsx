import React from "react";
import axios from "axios";

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
    axios
      .post("http://127.0.0.1:8000/recipe/find/", {
        user_input: this.state.question,
      })
      .then((response) => {
        this.props.onNewChatbotAnswer(response.data.recipe);
      })
      .catch((error) => {
        console.log(error);
      });
    //this.props.onNewChatbotAnswer("lorem lorem lorem lorem");
    this.setState({ question: "" });
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
