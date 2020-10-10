<template>
  <v-container>
    <v-card elevation="12">
      <v-row>
        
        <v-col cols="12" class="text-left">
          <v-btn
            elevation="18"
            style="z-index: 1;"
            class="white--text"
            outlined
            @click="dialog = true"
            :loading="dialog"
          >
            <v-icon>mdi-plus</v-icon>Yeni Kullanıcı
          </v-btn>
        </v-col>
      </v-row>
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
            fixed-header
            height="50vh"
            :headers="headers1"
            :items="this.getAllUsers"
            :sort-by="[]"
            :sort-desc="[]"
            :search="search"
            multi-sort
          >
            <template #item.index="{item}">
              <v-chip color="myColor" dark>{{ item.index }}</v-chip>
            </template>
            
            <template #item.actions="{item}">
              <v-icon @click="delete_us(item.id)" color="black"  >mdi-delete</v-icon>
            </template>
          </v-data-table>
        </v-col>
      </v-row>
    </v-card>

    <!-- ######################################### DİALOG BAŞLANGICI ######################################### -->
    <v-row justify="center">
      <v-dialog v-model="dialog" persistent scrollable max-width="600px">
        <v-form v-model="valid" ref="dialogCard">
          <v-card style="border-radius:12px;">
            <v-card-title class="myColor white--text">
              <span class="headline">Yeni Kullanıcı</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="6">
                    <v-text-field
                      :rules="rules.general"
                      hide-details="auto"
                      outlined
                      shaped
                      rounded
                      prepend-inner-icon="mdi-account"
                      label="Şirket İsmi*"
                      v-model="user.companyName"
                      required
                      counter="80"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-select
                      :items="types"
                      item-text="text"
                      item-value="value"
                      :rules="rules.type"
                      label="Kullanıcı Türü"
                      prepend-inner-icon="mdi-account-multiple"
                      outlined
                      rounded
                      v-model="user.isAdmin"
                      shaped
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field
                      :rules="rules.telNo"
                      hide-details="auto"
                      outlined
                      v-model="user.telNo"
                      label="Telefon Numarası*"
                      required
                      prefix="+90"
                      type="number"
                      counter="10"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field
                      :rules="rules.vergi"
                      hide-details="auto"
                      v-model="user.taxNo"
                      outlined
                      label="Vergi Numarası*"
                      required
                      type="number"
                      counter="10"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-textarea label="Adres*" v-model="user.companyAddress" counter="250" outlined :rules="rules.address"></v-textarea>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field
                      :rules="rules.email"
                      outlined
                      v-model="user.mail"
                      label="E-Posta*"
                      type="email"
                      required
                      counter="40"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field
                      :rules="rules.general"
                      hide-details="auto"
                      outlined
                      v-model="user.passwd"
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
              <v-spacer></v-spacer>
              <v-btn color="myColor" class="white--text" @click="closeDialog()">Kapat</v-btn>
              <v-btn
                color="myColor"
                :disabled="!valid"
                class="white--text"
                @click="save()"
              >Kaydet</v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
        <v-fade-transition>
          <v-overlay v-if="waitSave" z-index="9999">
            <v-progress-circular indeterminate size="64"></v-progress-circular>
          </v-overlay>
        </v-fade-transition>
      </v-dialog>
    </v-row>

    <!-- ######################################### DİALOG SONU ######################################### -->
    <v-snackbar
      v-model="snackSuccess"
      :timeout="snackTimeout"
      color="success"
      class="white--text"
    >
      Kullanıcı Başarıyla Eklendi!

    </v-snackbar>
    <v-snackbar
      v-model="snackError"
      :timeout="snackTimeout"
      color="error"
      class="white--text"
    >
      Kullanıcı Başarıyla Silindi!

    </v-snackbar>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Banner from "@/components/Banner";
export default {
  name: "Dashboard",
  components: {
    Banner
  },
  data() {
    return {
      snackTimeout: 3500,
      snackSuccess: false,
      snackError: false,
      waitSave: false,
      headers1: [
        {
          text: "Sıra",
          align: "start",
          sortable: false,
          value: "index"
        },
        { text: "İsim", value: "companyName" },
        { text: "Adres", value: "companyAddress" },
        { text: "E-Posta", value: "mail" },
        { text: "Vergi Numarası", value: "taxNo" },
        { text: "Tel No", value: "telNo" },
        { text: "Eylemler", value: "actions", sortable: false }
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
      title: "Tüm Kullanıcılar",
      dialog: false,
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
        type: [(v) => (!!v) || 'Gerekli Alan.'],
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
      types: [
        {text : "Müşteri" , value: "false"},
        {text : "Yönetici" , value: true},
      ],
      user: {
        companyName: "",
        companyAddress: "",
        mail: "",
        passwd: "",
        taxNo: "",
        telNo: "",
        isAdmin: ""
      }
    };
  },
  computed: {
    ...mapGetters(["getApplyArr", "getAllUsers"])
  },
  methods: {
    ...mapActions(["setApplyListApi", "get_users", "save_user", "delete_user"]),
    getColor(id) {
      if (id <= 3) return "red";
      else if (id <= 6) return "orange";
      else return "green";
    },
    closeDialog() {
      this.dialog = !this.dialog;
      this.$refs.dialogCard.reset();
    },
    save() {
      if (this.valid) {
        this.waitSave = true;
        this.save_user(this.user).then(() =>{
          this.waitSave = false;
          this.get_users();
          this.closeDialog();
        })
      }
      this.snackSuccess = true;
    },
    delete_us (id) {
      this.waitSave = true;
        this.delete_user(id).then(() =>{
          this.waitSave = false;
          this.get_users();
        })
      this.snackError = true;
    },
  },
  mounted() {
    this.get_users();
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