<template>
  <div
    id="modal"
    class="
      fixed
      top-0
      left-0
      w-screen
      h-screen
      flex
      items-center
      justify-center
      bg-blue-500 bg-opacity-50
      transform
      scale-0
      transition-transform
      duration-300
    "
    :class="show ? 'scale-100' : ''"
    style="overflow-y: scroll"
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
      <div>
				
			</div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      show: false,
      data: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    openModal() {
      this.show = true;
    },
    closeModal() {
      this.show = false;
    },
    async login(event) {
      event.preventDefault();
      const result = await AuthService.login(this.data);
      if (result.error) {
        console.log(result);
      } else {
        localStorage.setItem("access_token", result.access_token);
        this.$store.commit("storeAccessToken", result.access_token);
        this.$store.commit("storeIdUser", result.user_id);
        this.closeModal();
      }
    },
  },
};
</script>