<template>
  <div>
    <!-- ASİDE MENÜ BAŞI -->
    <v-navigation-drawer v-model="drawer" app dark class="asideMenu">
      <v-list light flat rounded shaped nav>
        <v-list-item dark class="pt-0 mt-0">
          <v-row justify="center" align="center" style="width:100%;">
            <v-col cols="12" class="pl-10">
              <v-list-item-content class="px-0 mx-0">
                <v-img class="mb-15" src="@/assets/logo2.png" />
              </v-list-item-content>
            </v-col>
          </v-row>
        </v-list-item>
        <v-list-group v-if="this.getIsAdmin" ripple prepend-icon="mdi-account">
          <template v-slot:activator>
            <v-list-item-title class="white--text">Kullanıcılar</v-list-item-title>
          </template>
          <v-list-item-group color="headerColor" mandatory>
            <v-list-item link exact exact-active-class="exactItem" class="white--text" dark id="allUsers" to="allUsers">
              <v-list-item-action>
                <v-icon medium>mdi-account-multiple</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Tüm Kullanıcılar</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list-group>

        <v-divider></v-divider>
        <v-list-group value="true" prepend-icon="mdi-folder">
          <template v-slot:activator>
            <v-list-item-title class="white--text">Başvurular</v-list-item-title>
          </template>
          <v-list-item-group color="headerColor">
            <v-list-item exact exact-active-class="exactItem" class="white--text" link dark id="allApplies" to="allApplies">
              <v-list-item-action>
                <v-icon medium>mdi-folder-multiple</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Tüm Başvurular</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link exact exact-active-class="exactItem" class="white--text" dark id="newApply" to="newApply">
              <v-list-item-action>
                <v-icon medium>mdi-folder-plus</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Başvuru Oluştur</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <!-- ASİDE MENÜ SONU -->

    <!-- TOPBAR MENÜ BAŞI -->
    <v-app-bar app light color="blue-grey lighten-5" height="45%">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-btn text rounded style="font-size:2.5vh;" color="blue">{{this.currentRouteName}}</v-btn>

      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn @click="logout" rounded elevation="24" dark color="#910330">
          <v-icon large class="pr-1">mdi-exit-to-app</v-icon>Çıkış
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>
    <!-- TOPBAR MENÜ BAŞI -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import router from "../router";
export default {
  name: "Aside",
  data() {
    return {
      menü1: true,
      drawer: null,
      items: [
        {
          icon: "mdi-bluetooth",
          text: "Bluetooth"
        },
        {
          icon: "mdi-chart-donut",
          text: "Data Usage"
        }
      ],
      model: 1
    };
  },
  computed: {
    ...mapGetters(["getIsAdmin", "getTitle"]),
    currentRouteName() {
      return this.$route.name;
    }
  },
  mounted() {},
  methods: {
    logout() {
      this.setIsAuthAct(false);
      router.push("/auth");
    },
    ...mapActions(["setIsAuthAct"]),
  }
};
</script>

<style>
i.v-icon.v-icon {
  color: whitesmoke;
}

.activeButton {
  background-color: aqua;
  outline-color: black;
}


.exactItem{
  background-color: #827397;
  color: antiquewhite;
  border-end-end-radius: 5px;

}

.asideMenu{
  background: rgb(2,0,36);
  background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(54,48,98,1) 50%, rgba(130,115,151,1) 100%);
}
</style>