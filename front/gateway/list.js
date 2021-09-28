import axios from 'axios';

const endpoint = process.env.ENDPOINT;

export class TwdougaListGateway {
  async get(offset, limit) {
    const params = {offset, limit}
    const query = Object.keys(params).map(key => `${key}=${params[key]}`).join('&');
    const url = query ? `${endpoint}list?${query}` : `${endpoint}list`;

    return (await axios.get(url)).data;
  }
}
