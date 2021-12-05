<template>
    <div>
        <div class="flex" 
            @mouseover="buttonAdd = true"
            @mouseleave="buttonAdd = false"
        >
            <p class="text-2xl font-bold cursor-pointer"
            >
                LANGUAGE
            </p>
            <button v-if="buttonAdd" @click="addChild()" class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 rounded">+</button>
        </div>
        <div
            class="ml-4"
        >
            <div class="mt-2 relative rounded-md" v-for="(l, index) in language" :key="index">
                <div class="flex"
                    @mouseover="buttonRemove = true"
                    @mouseleave="buttonRemove = false"
                >
                    <p class="text-lg text-black font-bold block w-full" contenteditable="true" placeholder="LANGUAGE">{{l.name}}</p>
                    <button v-if="buttonRemove" @click="removeChild(index)" class="bg-red-500 hover:bg-red-700 text-white font-bold px-2 rounded">-</button>
                </div>
                <p class="block w-full text-base" contenteditable="true" placeholder="Language detail">{{l.detail}}</p>            
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
            language: []
        }
    },
    methods: {
        addChild(){
            this.language.push({
                name: "",
                detail: ""
            })
        },
        removeChild(index){
           this.language.splice(index, 1)
        }
    },
}
</script>