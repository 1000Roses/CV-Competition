const API_URL = process.env.VUE_APP_API_URL

class ApiClient {
  constructor() {
    this.token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidHlwZSI6ImFjY2Vzc190b2tlbiIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ2YW50aWVuQGdtYWlsLmNvbSIsImV4cCI6MTYzODE2OTg2M30.AFANXSYpS22W7MVvRvHf-BJGl49-oT1O5osHQyqBcvU'
  }

  async get(endpoint) {
    const response = await fetch(`${API_URL}${endpoint}`, {
      headers: { Authorization: `Bearer ${this.token}` },
    })
    return response.json()
  }

  async post(endpoint, data) {
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
    const response = await fetch(`${API_URL}${endpoint}`, {
      method: 'DELETE',
      headers: { Authorization: `Bearer ${this.token}` },
    })
    return response.json()
  }
}

export default new ApiClient()
