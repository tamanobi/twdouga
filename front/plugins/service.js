import { TwdougaListGateway } from '~/gateway/list'
import { TwdougaListService } from '~/service/list'

export default function ({ $axios }, inject) {
  const service = {
    listService: getListService(),
  }
  inject('service', service)
}

function getListService() {
  const g = new TwdougaListGateway();
  return new TwdougaListService(g);
}
