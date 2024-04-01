import React from "react";
import Header from "./header";
import Chat from "./chat";
import UserInput from "./userInput";
export default class Chatbot extends React.Component{
    render(){
        return(
              <div className="columns-1 w-full flex flex-col min-h-screen justify-between pb-6 text-white md:min-h-desktop md:border-solid md:border-2 md:border-sky-500 md:w-11/12 md:mt-6 ">
                  <div>
                    <Header/>
                    <Chat/>
                  </div>
                    <UserInput/>
              </div>
        );
    }
}

