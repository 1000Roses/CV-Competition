<template>
  <div class="bg-body py-5">
    <br>
    <div
      id="cv"
      class="m-0 m-auto box-border grid grid-cols-2 bg-white"
    >
      <div class="col-span-2 mb-5"> 
        <div class="">
          <img
            src="https://i.imgur.com/uQxk5IK.png"
            alt=""
            class="rounded-full object-cover mx-auto"
          >
          <p class="text-center p-2 text-3xl font-semibold">
            LE VAN TIEN
          </p>
          <code class="flex justify-center"> Web, ML developer </code>
        </div>
      </div>
        
      <div class="col-span-1 left">
        <draggable
          :list="cv.leftData"
          group="people"
          item-key="name"
          @start="dragging = true"
          @end="dragging = false"
        >
          <!-- element is section -->
          <template #item="{ element }">  
            <div>
              <p class="text-2xl font-bold">
                {{ element.name }}
              </p>
              <div
                v-for="subSection in element.sub_section"
                :key="subSection"
                class="ml-4"
              >
                <p class="text-xl font-semibold p-2">
                  {{ subSection.name }}
                </p>
                <ul>
                  <li
                    v-for="content in subSection.content"
                    :key="content"
                  > 
                    <div
                      v-if="content.content != ''"
                      class="ml-4 p-2"
                    > 
                      <font-awesome-icon icon="code" /> {{ content.content }}
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </template>
        </draggable>
      </div>
      <div class="col-span-1 right"> 
        <draggable
          :list="cv.rightData"
          item-key="name"
          group="people"
          @start="dragging = true"
          @end="dragging = false"
        >
          <!-- element is section -->
          <template #item="{ element }">  
            <div>
              <p class="text-2xl font-bold">
                {{ element.name }}
              </p>
              <div
                v-for="subSection in element.sub_section"
                :key="subSection"
                class="ml-4"
              >
                <p class="text-xl font-semibold p-2">
                  {{ subSection.name }}
                </p>
                <ul>
                  <li
                    v-for="content in subSection.content"
                    :key="content"
                  > 
                    <div
                      v-if="content.content != ''"
                      class="ml-4 p-2"
                    > 
                      <font-awesome-icon icon="code" /> {{ content.content }}
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </template>
        </draggable>
      </div>
    </div>
    <br>
  </div>
</template>

<script>
import draggable from "vuedraggable"
import { CVService } from '../services'

export default {
    components: { draggable },
    data(){
      return {
        cv: {
          name : "",
          rightData: [],
          leftData : []
        },
        dataUpdate: [],
        controlOnStart: true,
        dragging: false
      }
    },
    watch : {
      "dragging" : {
        immediate: true,
        deep: true,
        handler(){
          this.updateCv()
        }
      },
    },
    created(){
      this.fetchCv()
    },
    methods : {
      clone({ name }) {
        return { name};
      },
      pullFunction() {
        return this.controlOnStart ? "clone" : true;
      },
      start({ originalEvent }) {
       this.controlOnStart = originalEvent.ctrlKey;
      },
      async fetchCv() {
        this.dataUpdate = await CVService.getCV(9)
        this.cv.name = this.dataUpdate.name
        for (var section of this.dataUpdate.section){
          if (section.column == 'right'){
            this.cv.rightData.push(section)
          } else {
            this.cv.leftData.push(section)
          }
        }
      },
      async updateCv() {
        if (this.dragging === true) {
          return
        }
        await this.syncDataUpdate()
        await CVService.updateCV(9, this.dataUpdate)
      },
      async syncDataUpdate(){
        for (var i = 0; i < this.cv.leftData.length; i++){
          this.cv.leftData[i].column = "left"
        }
        for (i = 0; i < this.cv.rightData.length; i++){
          this.cv.rightData[i].column = "right"
        }
        const synccore = () => {
          return this.cv.leftData.concat(this.cv.rightData)
        }
        this.dataUpdate.section = synccore()
      },
    }
}
</script>

<style scoped>
#cv {
  padding: 0.3in;
  width: 8.3in;
  height: 11.7in;
}
</style>
