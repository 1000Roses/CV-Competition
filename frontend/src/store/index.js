import { createStore } from 'vuex'

export default createStore({
  state: {
    idUser: "",
    accessToken : "",
    accountType : ""
  },
  mutations: {
    storeAccessToken(state, newAccessToken){
      state.accessToken = newAccessToken
    },
    resetToken(state){
      state.accessToken = ''
    },
    storeIdUser(state, id){
      state.idUser = id
    },
    resetIdUser(state){
      state.idUser = ''
    },
    storeAccountType(state, newAccountType){
      state.accountType = newAccountType
    },
    resetAccountType(state){
      state.accountType = ''
    }
  },
  actions: {
  },
  modules: {
  }
})
