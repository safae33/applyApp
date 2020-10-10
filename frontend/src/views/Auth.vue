<template>
  <v-app id="app">
    
      <v-parallax src="@/assets/bg.jpg" height="100vh">
      <v-row align="center" justify="center" style="height:100vh;">
      <v-col cols="10" xl="3" lg="6" md="6">
        <v-content style="background-color:blue-grey lighten-5;">
          <transition name="fade">
            <router-view></router-view>
          </transition>
        </v-content>
      </v-col>
      </v-row>
      </v-parallax>
    

  </v-app>
</template>

<script>
export default {
  name: "Auth",
  data: () => ({
    test: true
  })
};
</script>

<style>
@import '/../src/assets/style/animated.css';

.fade-enter-active {
  transition: opacity .5s;
}
.fade-leave-active{
   transition: opacity 0s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

v-image{
  filter: grayscale(100%);
}

</style>