<template>
  <v-footer dark fixed color="myColor" class="font-weight-medium" height="60vh" app>
    <v-row class="hidden-md-and-down">
      <v-col class="text-left" lg="6" md="6" xs="12" sm="12">
        <v-btn text elevation="24">
          {{ new Date().getFullYear() }} —
          <strong>Vue App Wuuhuuu</strong>
        </v-btn>
      </v-col>
      <v-col class="text-right" lg="6" md="6" xs="12" sm="12">
        <v-btn
          elevation="24"
          text
          href="https://www.foureng.net"
          target="_blank"
        >Designed by Foureng®</v-btn>
      </v-col>
    </v-row>

    <v-row class="hidden-sm-and-up">
      <v-col class="text-center mb-0 pb-3" lg="6" md="6" xs="12" sm="12">
        <v-btn x-small text elevation="12">
          {{ new Date().getFullYear() }} —
          <strong>Vue App Wuuhuuu</strong>
        </v-btn>
      </v-col>
      <v-col class="text-center mt-0 pt-0" lg="6" md="6" xs="12" sm="12">
        <v-btn
          elevation="12"
          text
          x-small
          href="https://www.foureng.net"
          target="_blank"
        >Designed by Foureng®</v-btn>
      </v-col>
    </v-row>
  </v-footer>

</template>

<script>
export default {
  name: "AppFooter"
};
</script>

<style>
.footer {
  z-index: 99999;
}
</style>