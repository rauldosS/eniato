import Axios from 'axios'
import { ENDPOINTS_CONSTANTS as URLS } from '../constants'

export default class ObjectiveRepository {
  constructor (requester = null, baseUri = null, factory = null) {
    this.requester = requester || Axios
    this.baseUri = baseUri || URLS.BASE_REST_URL
  }

  async getObjectiveList () {
    const uri = `${this.baseUri}/${URLS.GET_OBJECTIVE_LIST_FOR_AUTHENTICATED_USER_URL}`
    return this.requester.get(uri).then(({ data: dtoList }) => {
      return dtoList
    })
  }

  async save (data) {
    const uri = `${this.baseUri}/${URLS.SAVE_OBJECTIVE_URL}`
    const form = {
      id: data.id,
      value: data.value,
      balance: data.balance,
      name: data.name,
      objectiveDate: data.objectiveDate,
      description: data.description,
      color: data.color,
      icon: data.icon,
      status: data.objectiveStatus
    }

    return this.requester.post(uri, form).then(({ data: dto }) => {
      return dto
    })
  }

  async deactivate (objective) {
    const uri = `${this.baseUri}/${URLS.DEACTIVATE_OBJECTIVE_URL}`.replace('<objective-id>', objective.id)
    return this.requester.post(uri)
  }

  async activate (objective) {
    const uri = `${this.baseUri}/${URLS.ACTIVE_OBJECTIVE_URL}`.replace('<objective-id>', objective.id)
    return this.requester.post(uri)
  }

  async delete (objective) {
    const uri = `${this.baseUri}/${URLS.DELETE_OBJECTIVE_URL}`.replace('<objective-id>', objective.id)
    return this.requester.post(uri)
  }
}
