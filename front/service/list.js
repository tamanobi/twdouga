export class TwdougaListService {
  constructor(gateway) {
    this.gateway = gateway;
  }

  get(offset, limit) {
    return this.gateway.get(offset, limit);
  }
}
