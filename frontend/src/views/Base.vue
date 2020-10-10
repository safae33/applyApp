<template>
  <v-app v-if="isOkay" id="app">
    <Aside />

    <v-content style="background-color:blue-grey lighten-5;">
      <transition name="fade">
        <router-view v-if="isOkay"></router-view>
      </transition>
    </v-content>

    <!-- <AppFooter /> -->

    <!-- <v-system-bar app dark color="myColor" height="30vh">
      <v-row justify="center" align="center">
        <transition name="fade">
          <span>
            <v-icon>mdi-clock</v-icon>
            <input dark v-model="time" disabled />
          </span>
        </transition>
      </v-row>
    </v-system-bar>-->
  </v-app>
</template>

<script>
// import AppFooter from "@/components/Footer";
import Aside from "@/components/Aside";
import router from "../router";
import { mapGetters, mapActions } from "vuex";
// import Topbar from "@/components/Topbar";
export default {
  name: "Base",
  components: {
    // AppFooter,
    Aside
    // Topbar
  },
  computed: {
    ...mapGetters(["getIsAuth", "getApplyArr"]),
    
  },
  mounted() {
    if (!this.getIsAuth) {
      router.push("/auth");
    } else this.isOkay = true;
    //this.setApplyListApi();
    console.log(this.getApplyArr);
  },
  methods: {
    ...mapActions(["setApplyListApi"])
  },
  data: () => ({
    drawer: null,
    time: "",
    isOkay: false
  })
};
</script>

<style>
.fade-enter-active {
  transition: opacity 0.75s;
}
.fade-leave-active {
  transition: opacity 0s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>