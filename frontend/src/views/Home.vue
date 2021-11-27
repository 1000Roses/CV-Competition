<template>
  <div class="bg-body py-5">
      <br>
      <div class="w-1/2 mx-auto grid grid-cols-2 bg-cv py-5 px-8">
        <div class="col-span-2 mb-5"> 
            <div class= "">
                <img src="https://i.imgur.com/uQxk5IK.png"  alt="" class="rounded-full object-cover mx-auto">
                <p class="text-center p-2 text-3xl font-semibold">LE VAN TIEN</p>
                <code class="flex justify-center" > Web, ML developer </code>
            </div>
        </div>
        
        <div class="col-span-1 left">
          <draggable
          
            :list="cv.leftData"
          
            group="people"
            
            item-key="name"
          >
          <!-- element is section -->
            <template #item="{ element }">  
              <div>
                <p class="text-2xl font-bold"> {{ element.name }} </p>
                <div class="ml-4" v-for="subSection in element.sub_section" :key="subSection">
                  <p class="text-xl font-semibold p-2"> {{ subSection.name }} </p>
                  <ul>
                    <li v-for="content in subSection.content" :key="content"> 
                      <div v-if="content.content != ''" class="ml-4 p-2"> 
                        <font-awesome-icon  icon="code" /> {{ content.content }}
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
          >
          <!-- element is section -->
            <template #item="{ element }">  
              <div>
                <p class="text-2xl font-bold"> {{ element.name }} </p>
                <div class="ml-4" v-for="subSection in element.sub_section" :key="subSection">
                  <p class="text-xl font-semibold p-2"> {{ subSection.name }} </p>
                  <ul>
                    <li v-for="content in subSection.content" :key="content"> 
                      <div v-if="content.content != ''" class="ml-4 p-2"> 
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
import draggable from "vuedraggable";
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
        controlOnStart: true
      }
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
      async fetchCv(){
        var url = 'http://127.0.0.1:8000/cv/9/'
        const response = await fetch(url,{
          method: 'GET'
        })  
        if (response.ok && response.status === 200){
          this.dataUpdate = await response.json()
          this.cv.name = this.dataUpdate.name
          for (var section of this.dataUpdate.section){
            if (section.column == 'right'){
              this.cv.rightData.push(section)
            }else{
              this.cv.leftData.push(section)
            }
      
          }
        }
      },
      waitTime(){
        return new Promise((resolve) => {
          setTimeout(() => {
            resolve()
          }, 1000)
        })
      },
      async syncDataUpdate(){
        for (var i = 0; i < this.cv.leftData.length; i++){
          this.cv.leftData[i].column = "left"
        }
        for (i = 0; i < this.cv.rightData.length; i++){
          this.cv.rightData[i].column = "right"
        }
        console.log(this.cv.leftData)
        console.log(this.cv.rightData)
        const synccore = () => {
          return this.cv.leftData.concat(this.cv.rightData)
        }
        this.dataUpdate.section = synccore()
        console.log(this.dataUpdate.section)
      },
      async updateCv(){
        await this.syncDataUpdate()
        var url = 'http://127.0.0.1:8000/cv/9/'
        const response = await fetch(url,{
          method: 'PUT',
          headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidHlwZSI6ImFjY2Vzc190b2tlbiIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ2YW50aWVuQGdtYWlsLmNvbSIsImV4cCI6MTYzODA2OTMwOX0.X5AVPmMmIBAD_8LJuPHQPipIhCYSOcOlUjAwJSUr2CI"
          },
          body: JSON.stringify(this.dataUpdate)
        })  
        return response.json()
      }
    },
    created(){
      this.fetchCv()
    },
    watch : {
      "cv" : {
        immediate: true,
        deep: true,
        handler(){
          this.updateCv()
        }
      },
    }
}
</script>
