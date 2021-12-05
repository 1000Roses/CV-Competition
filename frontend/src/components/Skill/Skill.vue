<template>
    <div>
        <div class="flex" 
            @mouseover="buttonAdd = true"
            @mouseleave="buttonAdd = false"
        >
            <p class="text-2xl font-bold cursor-pointer" @click="openModal"
            >
                SKILLS
            </p>
            <button v-if="buttonAdd" @click="addSkill()" class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-2 rounded">+</button>
        </div>
        <div
        class="ml-4"
        >
        <div class="mt-2" v-for="(s, index) in skill" :key="index">
            <div class="flex"
                @mouseover="buttonRemove = true"
                @mouseleave="buttonRemove = false"
            >
                <p class="block w-full text-base" contenteditable="true" placeholder="Skill">{{s.name}}</p>
                <button v-if="buttonRemove" :initPercent="s.percent" @click="removeChild(index)" class="bg-red-500 hover:bg-red-700 text-white font-bold px-2 rounded">-</button>
            </div>
            <progress-bar></progress-bar>
        </div>
        </div>
    </div>
</template>

<script>
import ProgressBar from './ProgressBar.vue'
export default {
    data() {
        return {
            buttonAdd: false,
            buttonRemove: false,
            skill: []
        }
    },
    components:{
        ProgressBar
    },
    methods: {
        addSkill(){
            this.skill.push({
                name: "",
                percent: 0
            })
        },
        removeChild(index){
           this.skill.splice(index, 1)
        }
    },
}
</script>