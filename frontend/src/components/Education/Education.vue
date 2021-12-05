<template>
    <div>
        <div class="flex" 
            @mouseover="buttonAdd = true"
            @mouseleave="buttonAdd = false"
        >
            <p class="text-2xl font-bold cursor-pointer"
            >
                EDUCATION
            </p>
            <button v-if="buttonAdd" @click="addChild()" class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 rounded">+</button>
        </div>
        <div
            class="ml-4"
        >
            <div class="mt-2 relative rounded-md" v-for="(e, index) in education" :key="index">
                <div class="flex"
                    @mouseover="buttonRemove = true"
                    @mouseleave="buttonRemove = false"
                >
                    <p class="block w-full font-bold text-lg" contenteditable="true" placeholder="School name">{{e.name}}</p>
                    <button v-if="buttonRemove" @click="removeChild(index)" class="bg-red-500 hover:bg-red-700 text-white font-bold px-2 rounded">-</button>
                </div>
                <div class="flex items-center">
                    <p class="block text-sm" contenteditable="true" placeholder="Start date">{{e.start_date}}</p> &nbsp; &nbsp; - &nbsp; &nbsp;
                    <p class="block text-sm" contenteditable="true" placeholder="End date">{{e.end_date}}</p>
                </div>
                <p class="block w-full font-bold text-base" contenteditable="true" placeholder="Major">{{e.major}}</p>
                <p class="block w-full text-sm" contenteditable="true" placeholder="Study detail">{{e.detail}}</p>             
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
            education: []
        }
    },
    methods: {
        addChild(){
            this.education.push({
                name: "",
                detail: "",
                major: "",
                start_date: "",
                end_date: ""
            })
        },
        removeChild(index){
           this.education.splice(index, 1)
        }
    },
}
</script>