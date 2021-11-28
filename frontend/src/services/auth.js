import ApiClient from "./ApiClient"

class AuthService {
  async login(data) {
    const endpoint = `/user/login/`
    const response = await ApiClient.post(endpoint, data)
    if (!response.access_token) {
      throw new Error('Login failed')
    }
    return response
  }

  async register(data) {
    const endpoint = `/user/signup/`
    const response = await ApiClient.post(endpoint, data)
    // if (!response.access_token) {
    //   throw new Error('Sign up failed')
    // }
    return response
  }
}

export default new AuthService()
