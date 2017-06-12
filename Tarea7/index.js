import React from "react";
import ReactDOM from "react-dom";

var Greeting = React.createClass({
  render: function() {
    return (
      <div className="Greeting">
        Hello, {this.props.name}!
      </div>
    );
  }
});

  ReactDOM.render(
  <Greeting name="World"/>,
  document.getElementById('container')
);

console.log('Hello, world!');
