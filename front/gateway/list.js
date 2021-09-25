import axios from 'axios';

const endpoint = process.env.ENDPOINT;

export class TwdougaListGateway {
  async get() {
    const url = `${endpoint}list`;
    return (await axios.get(url)).data;
  }
}
