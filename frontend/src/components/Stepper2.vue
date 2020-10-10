<template>

  <v-stepper v-model="e1" color="grey lighten-5" non-linear alt-labels>
    <v-stepper-header>
      <v-stepper-step :complete="e1 > 1" step="1">Başvuru Bilgileri</v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step :complete="e1 > 2" step="2">Personel Listesi</v-stepper-step>
    </v-stepper-header>

    <v-stepper-items>
      <v-stepper-content step="1">
        <v-form v-model="newFormValid" ref="newApplyForm">
          <v-row justify="center">
            <v-row justify="center">
              <v-card elevation="6" width="95%">
                <v-card-title>
                  <v-icon style="color:black;">mdi-account</v-icon>Yetkili Bilgileri
                </v-card-title>

                <v-card-text width="100%">
                  <v-row>
                    <v-col cols="12" xl="3" lg="3" md="3" sm="6">
                      <v-text-field
                        :rules="rules.general"
                        hide-details="auto"
                        outlined
                        label="Yetkili İsmi*"
                        required
                        counter="80"
                        dense
                        disabled
                        v-model="apply.authName"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" xl="3" lg="3" md="3" sm="6">
                      <v-text-field
                        :rules="rules.tc"
                        hide-details="auto"
                        outlined
                        type="number"
                        label="Yetkili T.C. NO*"
                        required
                        counter="11"
                        dense
                        disabled
                        :value="apply.authTc"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" xl="3" lg="3" md="3" sm="6">
                      <v-text-field
                        :rules="rules.general"
                        hide-details="auto"
                        outlined
                        label="Yetkili Araç Plakası*"
                        required
                        dense
                        disabled
                        :value="apply.authPlaka"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" xl="3" lg="3" md="3" sm="6">
                      <v-text-field
                        :rules="rules.telNo"
                        hide-details="auto"
                        outlined
                        label="Telefon Numarası*"
                        required
                        prefix="+90"
                        type="number"
                        counter="10"
                        dense
                        disabled
                        :value="apply.authTel"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>

              <v-card elevation="6" width="95%" class="mt-5">
                <v-card-title>
                  <v-icon style="color:black;">mdi-factory</v-icon>Firma Bilgileri
                </v-card-title>

                <v-card-text width="100%">
                  <v-row>
                    <v-col cols="12" xl="6" lg="6" md="6" sm="6">
                      <v-text-field
                        :rules="rules.general"
                        hide-details="auto"
                        outlined
                        label="Şirket İsmi*"
                        required
                        counter="80"
                        dense
                        disabled
                        :value="apply.sirket"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" xl="6" lg="6" md="6" sm="6">
                      <v-text-field
                        :rules="rules.telNo"
                        hide-details="auto"
                        outlined
                        label="Telefon Numarası*"
                        required
                        prefix="+90"
                        type="number"
                        counter="10"
                        dense
                        disabled
                        :value="apply.sirketTel"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>

              <v-card elevation="6" width="95%" class="mt-5 mb-5">
                <v-card-title>
                  <v-icon style="color:black;">mdi-factory</v-icon>
                </v-card-title>

                <v-card-text width="100%">
                  <v-row>
                    <v-col cols="12" xl="6" lg="6" md="6" sm="6">
                      <v-textarea label="Adres*" counter="250" outlined :rules="rules.address" :value="apply.adres" disabled></v-textarea>
                    </v-col>
                    <v-col cols="12" xl="6" lg="6" md="6" sm="6">
                      <v-row>
                        <v-col cols="12" xl="12" lg="12" md="12" sm="12">
                          <v-text-field
                            :rules="rules.general"
                            hide-details="auto"
                            outlined
                            label="Faaliyeti*"
                            required
                            counter="80"
                            dense
                            disabled
                            class="mx-0 px-0"
                            :value="apply.duty"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" xl="12" lg="6" md="12" sm="12">
                          <v-switch
                            class="mt-0 pt-0"
                            v-model="apply.authName"
                            dense
                            disabled
                            label="Sanayi Sicil Belgesi var mı?"

                          ></v-switch>
                        </v-col>
                        <v-col cols="12" xl="12" lg="6" md="12" sm="12">
                          <v-text-field
                            v-if="sicilSwitch"
                            :rules="rules.general"
                            hide-details="auto"
                            outlined
                            label="Faaliyeti*"
                            required
                            counter="80"
                            dense
                            disabled
                            class="mx-0 px-0"
                          ></v-text-field>
                        </v-col>
                      </v-row>
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>

              <v-card elevation="6" width="95%" class="mx-0 px-0">
                <v-card-title>
                  <v-icon style="color:black;">mdi-factory</v-icon>Firma Bilgileri
                </v-card-title>

                <v-card-text width="100%">
                  <v-row>
                    <v-col cols="12" xl="3" lg="3" md="6" sm="6">
                      <v-text-field
                        :rules="rules.general"
                        hide-details="auto"
                        outlined
                        label="Yetkili İsmi*"
                        required
                        counter="80"
                        dense
                        disabled
                        :value="apply.authName"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" xl="3" lg="3" md="6" sm="6">
                      <v-dialog v-model="modalEdit" max-width="400px">
                        <template v-slot:activator="{on}">
                          <v-text-field
                            v-on="on"
                            dense
                            label="Düzenleme Tarihi "
                            v-model="dateEdit"
                            prepend-icon="mdi-calendar-range"
                            readonly
                            outlined
                            disabled
                            required
                          ></v-text-field>
                        </template>

                        <v-date-picker v-model="dateEdit" scrollable actions>
                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn text color="primary" @click="modalEdit = !modalEdit">Kaydet</v-btn>
                          </v-card-actions>
                        </v-date-picker>
                      </v-dialog>
                    </v-col>
                    <v-col cols="12" xl="3" lg="3" md="6" sm="6">
                      <v-dialog v-model="modalStart" max-width="400px">
                        <template v-slot:activator="{on}">
                          <v-text-field
                            v-on="on"
                            dense
                            label="Başlangıç Tarihi "
                            v-model="dateStart"
                            prepend-icon="mdi-calendar-range"
                            readonly
                            outlined
                            disabled
                            required
                          ></v-text-field>
                        </template>

                        <v-date-picker v-model="dateStart" scrollable actions>
                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn text color="primary" @click="modalStart = !modalStart">Kaydet</v-btn>
                          </v-card-actions>
                        </v-date-picker>
                      </v-dialog>
                    </v-col>
                    <v-col cols="12" xl="3" lg="3" md="6" sm="6">
                      <v-dialog v-model="modalEnd" max-width="400px">
                        <template v-slot:activator="{on}">
                          <v-text-field
                            v-on="on"
                            dense
                            label="Bitiş Tarihi "
                            v-model="dateEnd"
                            prepend-icon="mdi-calendar-range"
                            readonly
                            outlined
                            required
                            disabled
                          ></v-text-field>
                        </template>

                        <v-date-picker
                          v-model="dateEnd"
                          
                          scrollable
                          actions
                          color="deep-orange lighten-2"
                        >
                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn text color="primary" @click="modalEnd = !modalEnd">Kaydet</v-btn>
                          </v-card-actions>
                        </v-date-picker>
                      </v-dialog>
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>
            </v-row>

            
          </v-row>
        </v-form>
      </v-stepper-content>

      <v-stepper-content step="2">
        <v-row justify="center">
          <v-card elevation="6" width="95%" class="mt-2 mb-5 text-center">
            <v-card-title>
              <v-icon style="color:black;">mdi-factory</v-icon>Personel Bilgileri
            </v-card-title>

            <v-card-text width="100%" class="mb-5">
              <transition name="bounce">
                <v-row v-if="staffLength == 0" justify="center">
                  <v-alert
                    dense
                    border="left"
                    type="warning"
                  >Hiç personel eklemediniz. Bu şekilde devam ederseniz izin başvurunuz yalnızca şirket sahibi için geçerli olacaktır.</v-alert>
                </v-row>
              </transition>
              <transition-group name="fade">
                <v-row v-for=" i of this.staff" :key="i.id">
                  <v-col cols="12" xl="3" lg="3" md="3" sm="6">
                    <v-text-field
                      :rules="rules.general"
                      hide-details="auto"
                      outlined
                      label="Personel Ad-Soyad*"
                      required
                      counter="80"
                      dense
                      disabled
                      :value="i.staffName"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" xl="3" lg="3" md="3" sm="6">
                    <v-text-field
                      :rules="rules.tc"
                      hide-details="auto"
                      type="number"
                      outlined
                      label="Yetkili T.C. NO*"
                      required
                      counter="11"
                      dense
                      disabled
                      :value="i.staffTc"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" xl="3" lg="3" md="3" sm="6">
                    <v-text-field
                      :rules="rules.general"
                      hide-details="auto"
                      outlined
                      label="Personel Görevi*"
                      counter="80"
                      required
                      dense
                      disabled
                      :value="i.staffDuty"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" xl="3" lg="3" md="3" sm="6">
                    <v-text-field
                      :rules="rules.plaque"
                      hide-details="auto"
                      outlined
                      disabled
                      counter="10"
                      class="text-uppercase"
                      label="Araç Plaka*"
                      required
                      dense
                      :value="i.staffPlaka"
                    ></v-text-field>
                  </v-col>
 
                  <v-col cols="12">
                    <v-divider></v-divider>
                  </v-col>
                </v-row>
              </transition-group>
            </v-card-text>
          </v-card>

          


        </v-row>
      </v-stepper-content>
      
    </v-stepper-items>
  </v-stepper>
</template>

<script>
export default {
  name: "Stepper",
  props: {
      e1:Number
  },
  data() {
    return {
      newFormValid: false,
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
        tc: [
          value =>
            (value && value.length == 11) || "T.C. No 11 karakter olmalı."
        ],
        telNo: [
          value => (value && value.length == 10) || "Tel No 10 karakter olmalı."
        ],
        plaque: [
          value => !!value || "Gerekli Alan.",
          value => (value && value.length >= 3) || "En az 3 Karakter.",
          value =>
            (value && value.length <= 10) || "Plaka alanı 10 Karakteri geçemez."
        ],
        email: [
          v =>
            !v ||
            /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
            "E-Posta uygun olmalı."
        ]
      },
      dateEdit: "2020-07-02",
      dateStart: "2020-07-05",
      dateEnd: "2020-07-17",
      modalEdit: false,
      modalStart: false,
      modalEnd: false,

      finalCheck: false,
      sicilSwitch: false,

      staffLength: 1,

      title: "Yeni Başvuru",
      apply: {
        "index": "1",
        "authName": "Safa",
        "authTel": 5554443322,
        "authTc": 12312312312,
        "authPlaka": "06ab0606",
        "sirket": "Foureng",
        "sirketTel": "5551112233",
        "adres": "Bağlum/Keçiören",
        "duty": "Ekmek Dağıtımı",
        "sicil": false
      },
      staff: [
        {
          "id": "1",
          "staffName": "Emre YILDIRIM",
          "staffTc": "21323234326",
          "staffDuty": "Dağıtıcı",
          "staffPlaka": "06BG9874",
        },
        {
          "id": "2",
          "staffName": "Safa YILDIRIM",
          "staffTc": "29823264326",
          "staffDuty": "Dağıtıcı 2",
          "staffPlaka": "06Bt9234",
        },
      ],
    };
  },
  watch: {
    dialog() {
      this.$refs.newApplyForm.reset();
    }
  }
};
</script>

<style>
</style>