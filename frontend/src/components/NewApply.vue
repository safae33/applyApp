<template>
  <v-container class="mb-10">
    <v-card>

       
      <Banner />
      <v-card-text class="mt-5">
      <Stepper :e1="this.st" />
      </v-card-text>
      <v-card-actions>
            <v-row>
              <v-col cols="6" class="text-left pl-10">
            <v-btn color="myColor" dark @click="changee1(1)"><v-icon>mdi-arrow-left-box</v-icon>| İlk Sayfa</v-btn>
            <v-btn color="myColor" class="ml-5" dark @click="changee1(2)"><v-icon>mdi-arrow-right-box</v-icon>| İkinci Sayfa</v-btn>
              </v-col>
              <v-col cols="6" class="text-right pr-10">
            <v-btn color="myColor" class="ml-5" dark >Kaydet</v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import Banner from "@/components/Banner";
import Stepper from "@/components/Stepper";
export default {
  name: "Dashboard",
  components: {
    Banner,
    Stepper
  },
  data() {
    return {
      st:1,
      title:"Yeni Başvuru"
    };
  },
  watch: {
  },
  computed: {},
  mounted() {},
  methods: {
    changee1(i){
      this.st = i;
    }
  }
};
</script>

<style >
.top-col {
  position: fixed;
  height: 30vh;
  border-radius: 10px;
}

.data-col {
  position: relative;
}

.mdi-calendar-range {
  color: black;
}

.bounce-enter-active {
  animation: bounce-in .8s;
}

@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}



.fade-enter-active {
  transition: opacity 1s;
}
.fade-leave-active{
   transition: opacity 0s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>