export class TwdougaListService {
  constructor(gateway) {
    this.gateway = gateway;
  }

  get() {
    return this.gateway.get();
  }
}
