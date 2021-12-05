<template>
    <div class="relative pt-1">
    <div class="overflow-hidden h-2 text-xs flex rounded bg-purple-200" @mouseout="out">
        <div v-for="(item, index) in progress" :key="index"
            style="width: 20%"
            class="
                progress
                shadow-none
                flex flex-col
                text-center
                whitespace-nowrap
                text-white
                justify-center
                cursor-pointer
            "
            :class="item.show ? 'bg-purple-500': ''"
            @mouseover="hover(index)"
            @click="click(index)"
        ></div>
  </div>
</div>
</template>

<style scoped>

</style>

<script>
export default {
    props: [
        'initPercent'
    ],
    data(){
        return{
            progress:[
                {
                    show: false,
                },
                {
                    show: false,
                },
                {
                    show: false,
                },
                {
                    show: false,
                },
                {
                    show: false,
                },
            ],
            percent: this.initPercent || 0
        }
    },
    created() {
        this.setPercent(this.percent)
    },
    methods: {
        hover(index){
            this.setPercent(index);
        },
        out(){
            this.setPercent(this.percent);
        },
        click(index){
            this.percent = index;
        },
        setPercent(index){
            for(var i = 0; i <= 4; i++){
                if(i <= index){
                    this.progress[i].show = true;
                }else{
                    this.progress[i].show = false;
                }
            }
        }
    },
}
</script>