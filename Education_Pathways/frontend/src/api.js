import axios from 'axios';

export default axios.create({
  baseURL: "https://a1-docker.herokuapp.com/"
//   baseURL: "http://localhost:3000/"
});