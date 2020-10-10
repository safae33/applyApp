<template>
  <v-card>


      <v-form v-model="valid">
        <v-card>
          <v-card-title class="myColor white--text" >
            <span class="headline">Yeni Kullanıcı</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                  dense
                    :rules="rules.general"
                    hide-details="auto"
                    outlined
                    shaped
                    rounded
                    prepend-inner-icon="mdi-account"
                    label="Şirket İsmi*"
                    required
                    counter="80"
                  ></v-text-field>
                </v-col>

                <v-col cols="12" sm="6">
                  <v-text-field
                  dense
                    :rules="rules.telNo"
                    hide-details="auto"
                    outlined
                    label="Telefon Numarası*"
                    required
                    prefix="+90"
                    type="number"
                    counter="10"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field
                  dense
                    :rules="rules.vergi"
                    hide-details="auto"
                    outlined
                    label="Vergi Numarası*"
                    required
                    type="number"
                    counter="10"
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-textarea dense label="Adres*" counter="250" outlined :rules="rules.address"></v-textarea>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                  dense
                    :rules="rules.email"
                    outlined
                    label="E-Posta*"
                    type="email"
                    required
                    counter="40"
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                  dense
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
            </v-container>
            <v-label>*içeren alanlar doldurulmak zorundadır.</v-label>
          </v-card-text>
          <v-card-actions>
            
            <v-btn color="grey darken-2" dark to="/auth/login"><v-icon dark>mdi-left</v-icon> Girişe Dön</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="grey darken-2" dark>Kaydet</v-btn>
          </v-card-actions>
        </v-card>
      </v-form>

  </v-card>
</template>

<script>
export default {
  data() {
    return {
      valid: false,
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
            "E-Posta uygun olmalı."
        ]
      },
      types: ["Müşteri", "Yönetici"]
    };
  }
};
</script>

<style>
</style>