<template>
    <div class="bg-header p-4">
        <div class="flex mx-auto justify-between px-4">
            <div class="text-2xl font-semibold py-3">
                <div class="">
                    CV AWESOME 
                </div>
            </div>
            <div class="text-2xl font-semibold py-3 space-x-4" v-if="!login">
                <a href="#" @click="openLogin">Đăng nhập</a>
                <a href="#" @click="openRegister">Đăng ký</a>
            </div>
            <div class="text-2xl font-semibold py-3" v-if="login">
                <a href="#" @click="logout">Đăng xuất</a>
            </div>
        </div>
    </div>
    <modal-login ref="loginmodal"></modal-login>
    <modal-register ref="registermodal"></modal-register>
</template>

<script>
import ModalLogin from '../components/ModalLogin.vue'
import ModalRegister from '../components/ModalRegister.vue'
export default {
    data(){
        return{
            login: false
        }
    },
    components:{
        ModalLogin,
        ModalRegister
    },
    methods:{
        openLogin(){
            this.$refs.loginmodal.openModal()
        },
        openRegister(){
            this.$refs.registermodal.openModal()
        },
        logout(){
            this.$store.commit('resetToken');
            this.$store.commit('resetIdUser');
            this.login = false;
            this.$router.push({name:'Home'});
        }
    },
    watch : {
        '$store.state.accessToken' : function(){
            if (this.$store.state.accessToken != ""){
                this.login = true
            }
        }
    }
}
</script>