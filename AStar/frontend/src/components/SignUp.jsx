import React, { Component } from "react";
import axios from "axios"
import './css/SignUp.css'

class SignUp extends Component {

  constructor() {
    super();
    this.state = {
      username: "",
      password: ""
    };
    this.handleLogin = this.handleLogin.bind(this);
    this.handleUsernameChange = this.handleUsernameChange.bind(this);
    this.handlePasswordChange = this.handlePasswordChange.bind(this);
  }

  handleUsernameChange(event) {
    this.setState({username: event.target.value})
  }

  handlePasswordChange(event) {
    this.setState({password: event.target.value})
  }

  handleLogin(event) {
    event.preventDefault();
    this.createAccount(this.state.username, this.state.password)
  }

  createAccount = (username, password) => {
    axios.post(`https://astarchooser.herokuapp.com/user/register`, {
        'username': this.state.username,
        'password': this.state.password
    })
    .then(res => {
        console.log("create status: ", res.status)
        if (res.status === 200) {
            alert("Create Account Successfully!")
        }
        
    })
  }

  render() {
    // return ()
    return <div>Test</div>;
    
  }
}

export default SignUp;
