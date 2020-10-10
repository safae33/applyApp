<template>
  <v-card>
    <v-card-title class="myColor white--text" >
            <span class="headline">Şifre Sıfırlama</span>
          </v-card-title>
    <v-card-text class="pl-5 pr-5 pt-1">
      <v-form v-model="valid">
        <v-row align="center" justify="center">
          <v-col cols="12" xl="5" lg="5" md="9" sm="9">
            <v-img src="@/assets/ostim.png" />
          </v-col>
          <v-col cols="10">
            <v-label>Çalışma izni başvurusu yapabilmek için giriş yapmalsıınız.</v-label>
          </v-col>

          <v-col cols="12">
            <v-text-field
              :rules="rules.email"
              outlined
              label="E-Posta*"
              type="email"
              required
              counter="40"
              v-model="mail"
            ></v-text-field>
          </v-col>

        </v-row>
      </v-form>
    </v-card-text>
        <v-container fluid>
      <v-row class="text-center">
        <v-col cols="12">
          <v-btn :disabled="!valid" color="headerColor white--text">Şifre Hatırlat</v-btn>
        </v-col>

        <v-col cols="12">
          <v-divider></v-divider>
        </v-col>

        <v-col cols="12" >
          <v-btn to="/auth/login" color="grey darken-2 white--text">Girişe Geri Dön</v-btn>
        </v-col>

      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  data() {
    return{
      mail: "",
      valid:false,
            rules: {
        general: [
          value => !!value || "Gerekli Alan.",
          value => (value && value.length >= 3) || "En az 3 Karakter."
        ],
        address: [
          value => !!value || "Gerekli Alan.",
          value => (value && value.length >= 3) || "En az 3 Karakter.",
          value => (value && value.length <= 250) || "En Fazla 250 Karakter."
        ],
        type: [val => (val || "").length > 0 || "Gerekli Alan."],
        vergi: [
          value =>
            (value && value.length == 10) || "Vergi No 10 karakter olmalı."
        ],
        telNo: [
          value => (value && value.length == 10) || "Tel No 10 karakter olmalı."
        ],
        email: [
          v =>
            !v ||
            /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
            "E-Posta uygun olmalı.",
          value => !!value || "Gerekli Alan."
        ]
      }
    }
  }

}
</script>

<style>

</style>