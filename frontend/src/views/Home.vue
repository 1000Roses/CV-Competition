<template>
  <div class="bg-body py-5">
    <br />
    <button
      class="
        fixed
        right-10
        bottom-20
        bg-blue-500
        hover:bg-blue-700
        text-white
        font-bold
        px-2
        rounded
      "
      @click="savePDF"
    >
      Save PDF
    </button>
    <div id="cv" class="m-0 m-auto box-border flex flex-col bg-white">
      <div class="mb-5">
        <div class="flex items-center flex-col">
          <div class="">
            <div
              class="relative image flex items-center"
              @click="this.$refs.inputImage.click()"
            >
              <img
                v-if="srcImage"
                :src="srcImage"
                alt=""
                class="rounded-full object-cover image-profile"
              />
              <img
                v-else
                src="../assets/icon.png"
                alt=""
                class="rounded-full object-cover image-profile"
              />
              <img
                src="../assets/h.png"
                class="absolute left-20 image-camera"
              />
              <input
                ref="inputImage"
                accept="image/*"
                v-on:change="uploadImage"
                type="file"
                name="image-profile"
                hidden
              />
            </div>
          </div>
          <p
            class="text-center p-2 text-3xl font-semibold"
            contenteditable="true"
            placeholder="Name"
          >
            {{ profile_name }}
          </p>
          <code
            class="flex justify-center"
            contenteditable="true"
            placeholder="Position"
          >
            {{ major }}
          </code>
        </div>
      </div>
      <div class="flex flex-row">
        <div class="w-2/5">
          <div class="w-4/5">
            <div class="mb-2">
              <contact></contact>
            </div>
            <div class="mb-2">
              <skill></skill>
            </div>
            <div class="mb-2">
              <language></language>
            </div>
            <div class="mb-2">
              <prize></prize>
            </div>
            <!-- <draggable
            :list="cv.leftData"
            group="people"
            item-key="name"
            @start="dragging = true"
            @end="dragging = false"
          >
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
          </draggable> -->
          </div>
        </div>
        <div class="w-3/5">
          <div class="w-full">

            <div class="mb-2">
              <about-me></about-me>
            </div>
            <div class="mb-2">
              <work-ex></work-ex>
            </div>
            <div class="mb-2">
              <education></education>
            </div>
            <div class="mb-2">
              <project></project>
            </div>
            <!-- <draggable
            :list="cv.rightData"
            item-key="name"
            group="people"
            @start="dragging = true"
            @end="dragging = false"
          >
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
          </draggable> -->
          </div>
        </div>

      </div>
    </div>
    <br />
  </div>
</template>

<script>
// import draggable from "vuedraggable"
import { CVService } from "../services";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";
import Skill from "../components/Skill/Skill.vue";
import Contact from "../components/Contact/Contact.vue";
import Language from "../components/Language/Language.vue";
import Prize from "../components/Prize/Prize.vue";
import AboutMe from "../components/AboutMe/AboutMe.vue";
import WorkEx from "../components/WorkExperience/WorkExperience.vue";
import Education from "../components/Education/Education.vue";
import Project from "../components/Project/Project.vue";

export default {
  data() {
    return {
      srcImage: "",
      save: false,
      download: false,
      profile_name: "Nguyễn Việt Trung",
      major: "Web Developer",
      cv: {
        name: "",
        rightData: [],
        leftData: [],
      },
      dataUpdate: [],
      controlOnStart: true,
      dragging: false,
    };
  },
  components: {
    Skill,
    Contact,
    Language,
    Prize,
    AboutMe,
    WorkEx,
    Education,
    Project,
  },
  watch: {
    // "dragging" : {
    //   immediate: true,
    //   deep: true,
    //   handler(){
    //     this.updateCv()
    //   }
    // },
  },
  async created() {
    // await this.fetchCv();
    // this.savePDF()
  },
  methods: {
    clone({ name }) {
      return { name };
    },
    pullFunction() {
      return this.controlOnStart ? "clone" : true;
    },
    start({ originalEvent }) {
      this.controlOnStart = originalEvent.ctrlKey;
    },
    async fetchCv() {
      this.dataUpdate = await CVService.getCV(9);
      console.log(this.dataUpdate);
      this.cv.name = this.dataUpdate.name;
      for (var section of this.dataUpdate.section) {
        if (section.column == "right") {
          this.cv.rightData.push(section);
        } else {
          this.cv.leftData.push(section);
        }
      }
      // await this.svgToCanvas();
    },
    async updateCv() {
      if (this.dragging === true) {
        return;
      }
      await this.syncDataUpdate();
      await CVService.updateCV(9, this.dataUpdate);
    },
    async syncDataUpdate() {
      for (var i = 0; i < this.cv.leftData.length; i++) {
        this.cv.leftData[i].column = "left";
      }
      for (i = 0; i < this.cv.rightData.length; i++) {
        this.cv.rightData[i].column = "right";
      }
      const synccore = () => {
        return this.cv.leftData.concat(this.cv.rightData);
      };
      this.dataUpdate.section = synccore();
    },
    async savePDF() {
      this.save = true;
      this.download = true;
      const pdf = new jsPDF({
        format: "a4",
        orientation: "portrait",
        unit: "mm",
      });
      // pdf.html(document.getElementById('cv'), {
      //     html2canvas: {
      //         scale: 0.565 // default is window.devicePixelRatio
      //     },
      //     callback: function () {
      //         // pdf.save('test.pdf');
      //         window.open(pdf.output("bloburl"))
      //     }
      // });

      const canvas = await html2canvas(document.querySelector("#cv"));
      const imgData = canvas.toDataURL("image/png");
      const imgProps = pdf.getImageProperties(imgData);
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
      pdf.addImage(imgData, "PNG", 0, 0, pdfWidth, pdfHeight);
      pdf.save(`CV-${new Date().toLocaleDateString("vi-VN")}.pdf`);
      // window.open(pdf.output("bloburl"));
      // to debug
      // this.save = false;
    },
    uploadImage(event) {
      const file = event.target.files[0];
      this.srcImage = URL.createObjectURL(file);
    },
  },
};
</script>

<style scoped>
#cv {
  padding: 0.3in;
  width: 8.3in;
  height: 11.7in;
}
.image {
  width: 210px;
  height: 210px;
  cursor: pointer;
}
.image:hover > .image-profile {
  opacity: 0.2;
  z-index: 0;
}
.image-profile {
  z-index: 10;
}
.image-camera {
  z-index: 0;
  display: none;
}
.image:hover > .image-camera {
  display: block;
  text-align: center;
}
</style>
<style>
[contenteditable][placeholder]:empty:before {
  content: attr(placeholder);
  color: gray;
  background-color: transparent;
}
</style>