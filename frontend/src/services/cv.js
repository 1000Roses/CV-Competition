import ApiClient from "./ApiClient"

class CVService {
  async getCV(id) {
    const endpoint = `/cv/${id}/`
    const response = await ApiClient.get(endpoint)
    if (!response.id) {
      throw new Error('Get CV failed')
    }
    return response
  }

  async updateCV(id, data) {
    const endpoint = `/cv/${id}/`
    const response = await ApiClient.put(endpoint, data)
    if (response !== 'update successfully') {
      throw new Error('Update CV failed')
    }
    return response
  }
}

export default new CVService()
