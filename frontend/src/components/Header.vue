<template>
  <div class="p-4">
    <div class="flex mx-auto justify-between px-4">
      <div class="text-2xl font-semibold py-3">
        <div class="">
          CV AWESOME 
        </div>
      </div>
      <div
        v-if="!login"
        class="text-2xl font-semibold py-3 space-x-4"
      >
        <a
          href="#"
          @click="openLogin"
        >Đăng nhập</a>
        <a
          href="#"
          @click="openRegister"
        >Đăng ký</a>
      </div>
      <div
        v-if="login"
        class="text-2xl font-semibold py-3"
      >
        <a
          href="#"
          @click="logout"
        >Đăng xuất</a>
      </div>
    </div>
  </div>
  <modal-login ref="loginmodal" />
  <modal-register ref="registermodal" />
</template>

<script>
import ModalLogin from '../components/ModalLogin.vue'
import ModalRegister from '../components/ModalRegister.vue'

export default {
  components:{
    ModalLogin,
    ModalRegister
  },
  data() {
    return{
        login: this.$store.state.accessToken !== ""
    }
  },
  watch : {
    '$store.state.accessToken' : function(){
        if (this.$store.state.accessToken !== ""){
            this.login = true
        }
    }
  },
  methods:{
    openLogin(){
        this.$refs.loginmodal.openModal()
    },
    openRegister(){
        this.$refs.registermodal.openModal()
    },
    logout(){
      localStorage.removeItem('access_token')
      this.$store.commit('resetToken');
      this.$store.commit('resetIdUser');
      this.login = false;
      this.$router.push({name:'Home'});
    }
  }
}
</script>
