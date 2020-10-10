<template>
  <v-container>
    <v-card elevation="12">
      
      <Banner />
      <v-card-title class="pb-0 mb-0">
        <v-text-field
          dense
          dark
          v-model="search"
          append-icon="mdi-magnify"
          label="Arama"
          single-line
          outlined
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-row class="data-row d-inline">
        <v-col class="data-col" cols="12">
          <v-data-table
            :loading="this.getDataHere"
            fixed-header
            height="60vh"
            :headers="headers"
            :items="this.getApplyArr"
            :sort-by="[]"
            :sort-desc="[]"
            :search="search"
            multi-sort
            class="elevation-18"
            @click:row="handleClick"
          >
            <template #item.index="{item}">
              <v-chip color="myColor" dark>{{ item.index }}</v-chip>
            </template>
            <template #item.isApproved="{item}">
              <v-chip
                :color="isApprovedColor(item.isApproved)"
                dark
              >{{ item.isApproved ? "Onaylandı!" : "Onay Bekliyor..." }}</v-chip>
            </template>
            <template #item.state="{item}">
              <v-chip :color="stateColor(item)" dark>{{stateText(item)}}</v-chip>
            </template>
          </v-data-table>
        </v-col>
      </v-row>
    </v-card>
    <v-layout row justify-center>
      <v-dialog v-model="dialog" scrollable max-width="85vw">
        <v-card style="border-radius:12px;">
          <v-card-title class="myColor white--text" >
            <span class="headline">Başvuru Detayları</span>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <Stepper2 :e1="this.st" />
          </v-card-text>
          <v-card-actions>
            <v-row>
              <v-col cols="12" xl="6" lg="6" class="text-left pl-10">
            <v-btn color="myColor" dark @click="changee1(1)"><v-icon>mdi-arrow-left-box</v-icon>| İlk Sayfa</v-btn>
            <v-btn color="myColor" class="ml-5" dark @click="changee1(2)"><v-icon>mdi-arrow-right-box</v-icon>| İkinci Sayfa</v-btn>
              </v-col>
              <v-col cols="12" xl="6" lg="6"  class="text-right pr-10">
            <v-btn color="myColor" dark @click.native="dialog = false">Kapat</v-btn>
            <v-btn v-if="this.getIsAdmin" color="myColor" class="ml-5" dark >Onayla</v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Banner from "@/components/Banner";
import Stepper2 from "@/components/Stepper2";
export default {
  name: "Dashboard",
  components: {
    Banner,
    Stepper2
  },
  data() {
    return {
      st:1,
      dialog: false,
      headers: [
        {
          text: "Sıra",
          align: "start",
          sortable: false,
          value: "index"
        },
        { text: "Yetkili Ad-Soyad", value: "authNameSurname" },
        { text: "Yetkili Tel No", value: "authTelNo" },
        { text: "Yetkili Tc No", value: "authTc" },
        { text: "Onay Durumu", value: "isApproved" },
        { text: "Durum", value: "state" }
      ],
      desserts: [
        {
          name: "Frozen Yogurt",
          calories: 200,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: "1%"
        },
        {
          name: "Ice cream sandwich",
          calories: 200,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "1%"
        },
        {
          name: "Eclair",
          calories: 300,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: "7%"
        },
        {
          name: "Cupcake",
          calories: 300,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: "8%"
        },
        {
          name: "Gingerbread",
          calories: 400,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: "16%"
        },
        {
          name: "Jelly bean",
          calories: 400,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: "0%"
        },
        {
          name: "Lollipop",
          calories: 400,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: "2%"
        },
        {
          name: "Honeycomb",
          calories: 400,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: "45%"
        },
        {
          name: "Donut",
          calories: 500,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: "22%"
        },
        {
          name: "KitKat",
          calories: 500,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: "6%"
        }
      ],
      search: "",
      title: "Tüm Başvurular",
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
      types: ["Müşteri", "Yönetici"],
      clickedApply: "",
      
    };
  },

  computed: {
    ...mapGetters(["getApplyArr", "getDataHere", "getIsAdmin"])
  },
  methods: {
    ...mapActions(["setApplyListApi"]),
    isApprovedColor(check) {
      if (check) return "success";
      else return "grey";
    },
    stateColor(item) {
      if (item.isNew) return "success";
      else {
        if (item.isEnd) return "grey";
        else return "headerColor";
      }
    },
    stateText(item) {
      if (item.isNew) return "YENİ";
      else {
        if (item.isEnd) return "Tamamlanmış.";
        else return "Aktif Durumda";
      }
    },
    handleClick(value) {
      this.clickedApply = value;
      this.dialog = true;
    },
    changee1(i){
      this.st = i;
    }
  },
  mounted() {
    this.setApplyListApi();
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

.v-icon {
  color: black;
}
</style>