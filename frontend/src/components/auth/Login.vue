<template>
  <v-card>
    <v-card-title class="myColor white--text" >
            <span class="headline">Giriş Yap</span>
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
          <v-col cols="12">
            <v-text-field
              v-model="passwd"
              :rules="rules.general"
              hide-details="auto"
              outlined
              label="Parola*"
              type="password"
              required
              counter="20"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
    <v-container fluid>
      <v-row class="text-center">
        <v-col cols="12">
          <v-btn :disabled="!valid" @click="login" color="myColor white--text">Giriş Yap</v-btn>
        </v-col>
        <v-col cols="12">
          <transition name="bounce">
            <v-alert class="ml-5 mr-5" v-if="wrongCred" type="error">{{this.getErrMessage}}</v-alert>
          </transition>
        </v-col>
        <v-col cols="12">
          <v-divider></v-divider>
        </v-col>

        <v-col cols="12" xl="6" lg="6">
          <v-btn to="/auth/register" color="grey darken-2 white--text">Hemen Üye Ol</v-btn>
        </v-col>

        <v-col cols="12" xl="6" lg="6">
          <v-btn to="/auth/forgetPassword" color="grey darken-2 white--text">Şifremi unuttum</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import router from "../../router";
export default {
  data() {
    return {
      wrongCred: false,
      valid: false,
      mail: "",
      passwd: "",
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
    };
  },
  computed: {
    ...mapGetters(["getIsAuth", "getErrMessage"])
  },
  methods: {
    ...mapActions(["check_user"]),
    login() {
      this.check_user([this.mail, this.passwd]).then(() => {
        console.log(this.getIsAuth);
        if (this.getIsAuth) router.push("/");
        else {
          if (this.wrongCred) {  //hatalı kullanıcı uyarısı tekrar tekrar animasyonla verilsin ddiye bulduğum bi çözüm. zaten görünüyosa kaldıdrıp 200ms sonra tekrar true yapmak.
            this.wrongCred = false;

            setTimeout(() => {
              this.wrongCred = true;
            }, 200);
          } else this.wrongCred = true;
        }
      });
    }
  }
};
</script>

<style>
.bounce-enter-active {
  animation: bounce-in 0.8s;
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
</style>