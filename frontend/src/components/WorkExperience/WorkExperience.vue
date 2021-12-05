<template>
    <div>
        <div class="flex" 
            @mouseover="buttonAdd = true"
            @mouseleave="buttonAdd = false"
        >
            <p class="text-2xl font-bold cursor-pointer"
            >
                WORK EXPERIENCE
            </p>
            <button v-if="buttonAdd" @click="addChild()" class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 rounded">+</button>
        </div>
        <div
            class="ml-4"
        >
            <div class="mt-2 relative rounded-md" v-for="(w, index) in workex" :key="index">
                <div class="flex"
                    @mouseover="buttonRemove = true"
                    @mouseleave="buttonRemove = false"
                >
                    <p class="block w-full font-bold text-lg" contenteditable="true" placeholder="Company name">{{w.name}}</p>
                    <button v-if="buttonRemove" @click="removeChild(index)" class="bg-red-500 hover:bg-red-700 text-white font-bold px-2 rounded">-</button>
                </div>
                <div class="flex items-center">
                    <p class="block text-sm" contenteditable="true" placeholder="Start date">{{w.start_date}}</p> &nbsp; &nbsp; - &nbsp; &nbsp;
                    <p class="block text-sm" contenteditable="true" placeholder="End date">{{w.end_date}}</p>
                </div>
                <p class="block w-full font-bold text-base" contenteditable="true" placeholder="Job role">{{w.job_role}}</p>
                <p class="block w-full text-sm" contenteditable="true" placeholder="Job detail">{{w.detail}}</p>             
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            buttonAdd: false,
            buttonRemove: false,
            workex: []
        }
    },
    methods: {
        addChild(){
            this.workex.push({
                name: "",
                detail: "",
                start_date: "",
                end_date: ""
            })
        },
        removeChild(index){
           this.workex.splice(index, 1)
        }
    },
}
</script>