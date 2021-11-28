<template>
  <div
    id="modal"
    class="fixed top-0 left-0 w-screen h-screen flex items-center justify-center bg-blue-500 bg-opacity-50 transform scale-0 transition-transform duration-300"
    :class="show ? 'scale-100' : ''"
    style="overflow-y:scroll;"
  >
    <!-- Modal content -->
    <div class="fixed top-12 bg-white w-2/5 h-auto p-12"> 
      <!--Close modal button-->
      <button
        id="closebutton"
        type="button"
        class="focus:outline-none"
        @click="closeModal"
      >
        <!-- Hero icon - close button -->
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
      </button>
      <!-- Test content -->
      <form @submit="login">
        <div>
          <label
            class="block text-gray-700 text-lg font-bold mb-2"
            for="email"
          >
            Email
          </label>
          <input
            id="email"
            v-model="data.email"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            type="email"
            placeholder="Email"
            required
          >
        </div>
        <div class="mb-5">
          <label
            class="block text-gray-700 text-lg font-bold mb-2"
            for="password"
          >
            Password
          </label>
          <input
            id="password"
            v-model="data.password"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            type="password"
            placeholder="Password"
            required
          >
        </div>
        <div class="flex items-center justify-between">
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            Sign In
          </button>
          <a
            class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800"
            href="#"
          >
            Forgot Password?
          </a>
        </div>
      </form>            
    </div>
  </div>
</template>

<script>
export default {
	data(){
		return{
			show: false,
            data: {
                email: "",
                password: ""
            }
		}
	},
	methods: {
		openModal(){
			this.show = true;
		},
		closeModal(){
			this.show = false;
		},
        async login(event){
            event.preventDefault();
            const url = 'http://127.0.0.1:8000/user/login/';
            
            const response = await fetch(url, {
                method: 'POST',
                headers:{
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(this.data)
            })

            if(response.ok && response.status === 200){
                const result = await response.json()
                console.log(result)
                if(result.error){
                    console.log(result);
                }else{
                    this.$store.commit('storeAccessToken', result.access_token)
                    this.$store.commit('storeIdUser', result.user_id)
                    this.closeModal()
                }
            }

        }  
    },
}
</script>