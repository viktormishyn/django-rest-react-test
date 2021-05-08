import React from "react";

class connectionExample extends React.Component {
  componentDidMount() {
    const apiUrl = "http://127.0.0.1:8000/api/";
    fetch(apiUrl)
      .then((res) => res.json())
      .then((data) => console.log(data));
  }
  render() {
    return <div>Example connection</div>;
  }
}

export default connectionExample;
