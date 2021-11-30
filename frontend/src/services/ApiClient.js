const API_URL = process.env.VUE_APP_API_URL

function getToken() {
  return localStorage.getItem('access_token') || ''
}

class ApiClient {
  constructor() {
    this.token = ''
  }

  async get(endpoint) {
    this.token = getToken()
    const response = await fetch(`${API_URL}${endpoint}`, {
      headers: { Authorization: `Bearer ${this.token}` },
    })
    return response.json()
  }

  async post(endpoint, data) {
    this.token = getToken()
    const response = await fetch(`${API_URL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
        Authorization: `Bearer ${this.token}`,
      },
      body: JSON.stringify(data),
    })
    return response.json()
  }

  async put(endpoint, data) {
    this.token = getToken()
    const response = await fetch(`${API_URL}${endpoint}`, {
      method: 'PUT',
      headers: {
        'Content-type': 'application/json',
        Authorization: `Bearer ${this.token}`,
      },
      body: JSON.stringify(data),
    })
    return response.json()
  }

  async delete(endpoint) {
    this.token = getToken()
    const response = await fetch(`${API_URL}${endpoint}`, {
      method: 'DELETE',
      headers: { Authorization: `Bearer ${this.token}` },
    })
    return response.json()
  }
}

export default new ApiClient()
